# Financial Performance & Budget Dashboard

A finance analytics portfolio project for reviewing monthly revenue, operating costs, gross margin, cash flow, and budget variance.

## Business questions

- Did revenue meet the budget each month?
- Which cost centres exceeded plan?
- How did gross margin and operating cash flow perform?
- Which months require management attention?

## Project contents

```text
financial-performance-budget-dashboard/
├── data/sample/              # Synthetic monthly finance data
├── outputs/tables/           # KPI and variance extracts
├── outputs/charts/           # Dashboard visuals
├── sql/                      # PostgreSQL-compatible analysis queries
└── src/                      # Reproducible Python workflow
```

## Results

| KPI | FY2025 result |
| --- | ---: |
| Revenue | 7.84M |
| Revenue versus budget | +2.9% |
| Operating costs | 5.15M |
| Cost versus budget | +1.7% |
| Gross margin | 34.3% |
| Operating cash flow | 1.34M |

The analysis identifies a revenue shortfall in August and overspend in Operations, while Technology spend stayed below plan.

## Run the project

```bash
pip install -r requirements.txt
python src/analyze_finance.py
```

## Dashboard

View the interactive dashboard: https://finance-budget-dashboard.mammadov-mammad10.chatgpt.site

## Tools

- Python, pandas, matplotlib
- SQL
- Power BI-ready CSV outputs

## Data note

The data is synthetic and designed only for portfolio practice. It does not use confidential financial information.
