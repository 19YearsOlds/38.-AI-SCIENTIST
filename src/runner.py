import json
from pathlib import Path
from . impoort loaders, parser, dataset_utils, experiments, analysis, propose, config, utils

def pipeline_from_pdf(pdf_path: str):
    p = Path(pdf_path)
    print(f"Loading {p}")
    text = loaders.load_pdf_text(p)
    sections = parser.split_sections(text)

    X, y = dataset_utils.synthetic_regression(n=200, dim=8, noise=0.2, seed=config.DEFAULT_SEED)

    exp_name = p.stem.replace(" ", "_")
    res = experiments.run_simple_regression(X, y, exp_name=exp_name, save=True)

    out_dir = Path(config.EXP_DIR) / exp_name
    y_test = (out_dir / "y_test.npy").exists() and utils.load_npy(out_dir / "y_test.npy")
    y_pred = (out_dir / "y_pred.npy").exists() and utils.load_npy(out_dir / "y_pred.npy")

    if y_test is not False and y_pred is not False:
        summary = analysis.summarize_predictions(y_test, y_pred)
    else:
        summary = res

    sections_text = "\n\n".join([f"{k}:\n{v[:1000]}" for k,v in sections.items()])
    hyps = propose.generate_hypothesis(sections_text, json.dumps(summary))

    out = {
        "paper": str(p),
        "sections": list(sections.keys()),
        "experiment": res,
        "analysis": summary,
        "hypotheses": hyps
    }
    with open(out_dir / "report.json", "w") as f:
        json.dump(out, f, indent=2)
    print("Pipeline complete:", out_dir / "report.json")
    return out

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python -m src.runner path/to.paper.pdf")
        sys.exit(1)
    pipeline_from_pdf(sys.argv[1])