-- 1. Top 5 Funds by AUM
SELECT scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;


-- 2. Average NAV Across All Funds
SELECT AVG(nav) AS avg_nav
FROM fact_nav;


-- 3. Total SIP Transactions
SELECT COUNT(*) AS sip_transactions
FROM fact_transactions
WHERE transaction_type = 'SIP';


-- 4. Transactions by State
SELECT state,
       COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;


-- 5. Funds with Expense Ratio Below 1%
SELECT scheme_name,
       expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;


-- 6. Top 5 Performing Funds (1-Year Return)
SELECT scheme_name,
       return_1yr_pct
FROM fact_performance
ORDER BY return_1yr_pct DESC
LIMIT 5;


-- 7. Average Expense Ratio
SELECT AVG(expense_ratio_pct) AS avg_expense_ratio
FROM fact_performance;


-- 8. Fund Category Distribution
SELECT category,
       COUNT(*) AS total_funds
FROM fact_performance
GROUP BY category
ORDER BY total_funds DESC;


-- 9. Average Transaction Amount by Type
SELECT transaction_type,
       AVG(amount_inr) AS avg_amount
FROM fact_transactions
GROUP BY transaction_type;


-- 10. Highest AUM Fund
SELECT scheme_name,
       aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 1;