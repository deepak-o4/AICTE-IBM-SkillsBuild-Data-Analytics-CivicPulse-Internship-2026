from src.civicpulse_pipeline import run_project


if __name__ == "__main__":
    result = run_project()
    print("CivicPulse project successfully generated.")
    print("Summary KPIs:")
    for key, value in result["kpis"].items():
        if key not in {"yearly_counts", "status_counts", "category_top_10", "ward_top_10"}:
            print(f"- {key}: {value}")
    print("Figures generated:")
    for name in result["figures"].values():
        print(f"- {name}")
