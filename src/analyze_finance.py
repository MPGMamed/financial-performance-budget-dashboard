"""Create reproducible finance KPI tables and dashboard charts."""
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]

def main() -> None:
    finance = pd.read_csv(ROOT / "data/sample/monthly_finance.csv", parse_dates=["month"])
    departments = pd.read_csv(ROOT / "data/sample/department_costs.csv")
    tables = ROOT / "outputs/tables"
    charts = ROOT / "outputs/charts"
    tables.mkdir(parents=True, exist_ok=True)
    charts.mkdir(parents=True, exist_ok=True)

    finance["revenue_variance"] = finance["revenue_actual"] - finance["revenue_budget"]
    finance["cost_variance"] = finance["operating_cost_actual"] - finance["operating_cost_budget"]
    finance["gross_margin"] = (finance["revenue_actual"] - finance["operating_cost_actual"]) / finance["revenue_actual"]
    departments["variance"] = departments["actual_cost"] - departments["budget_cost"]
    finance.to_csv(tables / "monthly_performance.csv", index=False)
    departments.to_csv(tables / "department_variance.csv", index=False)

    kpis = pd.DataFrame([
        ("Revenue", finance.revenue_actual.sum()),
        ("Revenue variance", finance.revenue_variance.sum()),
        ("Operating costs", finance.operating_cost_actual.sum()),
        ("Cost variance", finance.cost_variance.sum()),
        ("Gross margin", (finance.revenue_actual.sum() - finance.operating_cost_actual.sum()) / finance.revenue_actual.sum()),
        ("Operating cash flow", finance.operating_cash_flow.sum()),
    ], columns=["metric", "value"])
    kpis.to_csv(tables / "kpi_summary.csv", index=False)

    plt.style.use("seaborn-v0_8-whitegrid")
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(finance.month, finance.revenue_actual / 1_000_000, marker="o", label="Actual", color="#2458d5")
    ax.plot(finance.month, finance.revenue_budget / 1_000_000, marker="o", label="Budget", color="#b9c4dd")
    ax.set(title="Monthly Revenue versus Budget", ylabel="Millions", xlabel="2025")
    ax.legend()
    fig.autofmt_xdate()
    fig.tight_layout()
    fig.savefig(charts / "revenue_vs_budget.svg")
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(9, 5))
    ranked = departments.sort_values("variance")
    ax.barh(ranked.department, ranked.variance / 1_000_000, color=["#167d56" if value < 0 else "#d79922" for value in ranked.variance])
    ax.axvline(0, color="#172238", linewidth=0.8)
    ax.set(title="Department Cost Variance to Budget", xlabel="Millions, actual less budget")
    fig.tight_layout()
    fig.savefig(charts / "department_cost_variance.svg")
    plt.close(fig)
    print("Finance KPI tables and charts created.")

if __name__ == "__main__":
    main()
