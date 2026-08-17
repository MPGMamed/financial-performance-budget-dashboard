-- Monthly performance against budget
SELECT
    month,
    revenue_actual,
    revenue_budget,
    revenue_actual - revenue_budget AS revenue_variance,
    operating_cost_actual - operating_cost_budget AS cost_variance,
    ROUND(100.0 * (revenue_actual - operating_cost_actual) / revenue_actual, 1) AS gross_margin_pct,
    operating_cash_flow
FROM monthly_finance
ORDER BY month;

-- Cost-centre variance review
SELECT
    department,
    actual_cost,
    budget_cost,
    actual_cost - budget_cost AS variance_to_budget,
    ROUND(100.0 * (actual_cost - budget_cost) / budget_cost, 1) AS variance_pct
FROM department_costs
ORDER BY variance_to_budget DESC;
