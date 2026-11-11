# Datheon — Task 1: EDA — Superstore Retail Sales

Author: Mehak Jilani | Internship: Data Analytics & Power BI (Cohort 2026)
Notebook: Superstore_Retail_Sales_EDA.ipynb
Data: superstore_clean.csv (9,994 rows x 26 cols)

## How to run
1. Open Superstore_Retail_Sales_EDA.ipynb in Google Colab
2. Upload superstore_clean.csv in same folder
3. Runtime -> Run All

## What the EDA covers
1. Setup + Data Overview (missing = 0, duplicates = 0)
2. Cleaning log (dates parsed, Margin + Discount Band created)
3. KPIs: Sales $2,297,201, Profit $286,397, Margin 12.47%, Orders 5,009
4. Yearly Trend: 2016 -2.8%, 2017 +29.5%, 2018 peak $733,215
5. Category: Technology profit engine (17.40%), Furniture trap (2.49%)
6. Sub-Category: Top = Copiers $55,618 | Loss only in Tables, Bookcases, Supplies
7. Region: West + East = 61% sales
8. Segment: Consumer = 50.6% sales
9. Discount: >20% = loss in every band, total -$135,376

## Key Findings
- Discount >20% is loss-making — cap at 20%
- Furniture $741,999 sales -> only $18,451 profit
- Technology + Office Supplies = 93.6% of total profit
