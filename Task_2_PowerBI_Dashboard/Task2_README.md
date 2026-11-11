# Datheon — Task 2: Power BI Dashboard — Superstore Executive Sales & Profit

Author: Mehak Jilani | Internship: Data Analytics & Power BI (Cohort 2026)
Period: 2015-2018 | Data: superstore_clean.csv (9,994 rows)

## Files in this folder
- PowerBI_Dashboard_index.html — Live Interactive Dashboard (open in browser)
- Task2_Executive_Dashboard_Report.pdf — Exported Executive Report (3 pages)
- Task2_DAX_Measures.txt — All DAX Measures

## How to open Dashboard
1. PowerBI_Dashboard_index.html ko download karo
2. Browser me kholo (Chrome) — koi install nahi chahiye
3. Date & Region filters use karo

## How to build .pbix on PC
1. Power BI Desktop -> Get Data -> superstore_clean.csv
2. Model: Fact_Orders -> Dim_Customer, Dim_Product, Dim_Date (Star Schema)
3. Modeling -> New Measure -> Task2_DAX_Measures.txt se paste karo
4. Pages: 1. Overview 2. Product 3. Regional & Discount

## KPIs
Total Sales: $2,297,201 | Total Profit: $286,397 | Margin: 12.47%
Orders: 5,009 | Avg Order Value: $458.61

## Key Findings
- Technology = Profit Engine — $836,154 sales -> $145,455 profit (17.40%)
- Furniture = Revenue Trap — $741,999 sales -> only $18,451 profit (2.49%)
- Discount >20% = Loss in every band — Total loss -$135,376
- West + East = 61% sales | Central lowest margin 7.92%
