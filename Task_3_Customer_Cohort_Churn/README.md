Datheon Task 3 — Customer Cohort & Churn Analytics
Dataset: IBM Telco Churn — 7,043 customers, 21 columns
Tools: Python (Pandas, Matplotlib, Seaborn), HTML Dashboard
Live Dashboard: Churn_Dashboard_index.html — open in browser / GitHub Pages

Key Findings (verified from dataset)
Metric	Value
Total Customers	7,043
Churned	1,869
Retained	5,174
Baseline Churn Rate	26.5%
1. Tenure Cohort — New customers leave fastest
Cohort	Customers	Churn Rate
0-12 months	2,186	47.4%
13-24 months	1,024	28.7%
25-36 months	832	21.6%
37-48 months	762	19.0%
49-60 months	832	14.4%
61-72 months	1,407	6.6%
Insight: Churn falls as tenure rises. First year is the danger zone.

2. Contract — Biggest lever
Contract	Churn Rate
Month-to-month	42.7%
One year	11.3%
Two year	2.8%
3. High-Risk Segments
Fiber Optic + No Tech Support: 49.4% churn (2,230 customers)
Month-to-month + No Tech Support: 50.4% churn (2,680 customers)
Electronic check payment: 45.3% churn vs Credit card (automatic): 15.2%
4. Churned vs Retained
Churned: avg tenure 18.0 months, avg MonthlyCharges $74.44
Retained: avg tenure 37.6 months, avg MonthlyCharges $61.27
Churned customers pay MORE but stay LESS — value perception problem.
Data Cleaning
TotalCharges: 11 blank strings (tenure = 0, new customers) → converted to numeric, filled with 0.
No duplicates. No other nulls.
Strategic Retention Recommendations
First-90-days onboarding: 0-12 month cohort = 47.4% churn. Welcome call + setup help + first-bill explainer in first 30 days.
Move Month-to-month → Annual: Month-to-month churn 42.7% vs Two-year 2.8%. Offer 1-month free / discount to lock 1-year contract at month 3-6.
Bundle Tech Support with Fiber: Fiber + No Tech Support = 49.4% churn. Free Tech Support for first 3 months for every new Fiber customer.
Migrate Electronic check → Auto-pay: Electronic check churn 45.3% vs auto-pay ~15-17%. Auto-pay discount + reminder before due date.
Save-play for high MonthlyCharges: Churned pay $74.44 vs retained $61.27. Proactive retention offer (plan downgrade / loyalty discount) when MonthlyCharges > $85 and tenure < 12 months.
Files
Task3_Churn_Analysis.py — full analysis (run it to reproduce all numbers)
Churn_Dashboard_index.html — interactive dashboard (cohort matrix, contract, payment, risk)
requirements.txt — pandas, matplotlib, seaborn, numpy
How to run
pip install -r requirements.txt
python Task3_Churn_Analysis.py
