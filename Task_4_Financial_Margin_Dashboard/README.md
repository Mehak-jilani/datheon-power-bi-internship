Task 4 — Corporate Financial & Margin Performance Dashboard | Datheon Internship
Track quarterly revenue, COGS, discounts, and operating margins across corporate divisions — with a waterfall from Gross Sales to Profit, segment / product / country margins, and interactive scenario forecasting.

Dataset
File: Financial_Sample.xlsx — Microsoft Financial Sample (Excel, Sheet1)
Rows: 700 | Columns: 16
Date range: Sep 2013 to Dec 2014
Columns: Segment, Country, Product, Discount Band, Units Sold, Manufacturing Price, Sale Price, Gross Sales, Discounts, Sales (Net Sales), COGS, Profit, Date, Month Number, Month Name, Year
Cleaning
Trimmed the Sales column header to Sales (Net Sales).
Discount Band: 53 blanks filled with None (no discount).
Duplicates: 0 | Other nulls: 0.
Key Results — Waterfall (Gross Sales → Profit)
Step	Amount
Gross Sales	$127,931,598.50
Less: Discounts	-$9,205,248.24 (7.20% of Gross)
= Net Sales	$118,726,350.26
Less: COGS	-$101,832,648.00 (85.77% of Net Sales)
= Profit	$16,893,702.26
Gross Profit % (Margin on Net Sales): 14.23%
COGS Ratio: 85.77%
Margin on Gross Sales: 13.21%
Negative-profit rows: 58 / 700
Margin by Segment
Segment	Net Sales	Profit	Margin %	COGS %
Channel Partners	$1,800,593.64	$1,316,803.14	73.13%	26.87%
Midmarket	$2,381,883.08	$660,103.07	27.71%	72.29%
Government	$52,504,260.67	$11,388,173.17	21.69%	78.31%
Small Business	$42,427,918.50	$4,143,168.50	9.77%	90.23%
Enterprise	$19,611,694.38	-$614,545.62	-3.13%	103.13%
Finding: Enterprise is loss-making — its COGS (103.13%) exceeds its Net Sales. Channel Partners is the most profitable segment by margin, Government drives the largest absolute profit.

Margin by Product
Product	Net Sales	Profit	Margin %
Amarilla	$17,747,116.06	$2,814,104.06	15.86%
VTT	$20,511,921.02	$3,034,608.02	14.79%
Paseo	$33,011,143.95	$4,797,437.95	14.53%
Montana	$15,390,801.88	$2,114,754.88	13.74%
Carretera	$13,815,307.88	$1,826,804.88	13.22%
Velo	$18,250,059.46	$2,305,992.46	12.64%
Margin by Country
Country	Net Sales	Profit	Margin %
Germany	$23,505,340.82	$3,680,388.82	15.66%
France	$24,354,172.28	$3,781,020.78	15.53%
Canada	$24,887,654.88	$3,529,228.88	14.18%
Mexico	$20,949,352.11	$2,907,523.11	13.88%
United States of America	$25,029,830.16	$2,995,540.66	11.97%
Discount vs Margin — the Waterfall Story
Discount Band	Net Sales	Profit	Margin %
None	$7,943,654.00	$1,736,455.00	21.86%
Low	$34,629,778.70	$6,188,857.70	17.87%
Medium	$38,780,430.84	$5,579,522.84	14.39%
High	$37,372,486.72	$3,388,866.72	9.07%
Finding: As discount rises, margin falls — High discount earns the second-highest Net Sales but the lowest margin. Discounts erode $9.2M before COGS is even charged.

Margin by Quarter / Year
Period	Net Sales	Profit	Margin %
2013	$26,415,255.51	$3,878,464.51	14.68%
2014	$92,311,094.75	$13,015,237.75	14.10%
Q1	$19,492,152.94	$2,632,442.94	13.51%
Q2	$22,693,879.95	$3,232,378.45	14.24%
Q3	$24,850,239.87	$3,501,667.37	14.09%
Q4	$51,690,077.50	$7,527,213.50	14.56%
Note: the file covers Sep–Dec 2013 only (not a full year), so 2013 vs 2014 is not a like-for-like year comparison. Q4 has more rows (315) than other quarters, which inflates its total.

Budget / Variance — Important Assumption
The Excel has NO Budget / Target column. So true Actual-vs-Budget variance cannot be computed from the data itself.

In Power BI, variance is shown against a What-If Budget Sales Target parameter (default $120,000,000, adjustable with a slider). See Task4_DAX_Measures.txt:

Budget Sales, Sales Variance vs Budget, Sales Variance % vs Budget
Forecast Net Sales / Forecast Profit use a Growth % What-If parameter (-20% to +50%, default +10%).
State this assumption on the dashboard — do not present the What-If target as a Budget column from the dataset.

Files
File	What it is
Financial_Sample.xlsx	Source dataset (Microsoft Financial Sample)
Task4_Financial_Analysis.py	Python analysis — waterfall, segment / product / country / quarter margins
Task4_DAX_Measures.txt	Power BI DAX — Gross Profit %, COGS Ratio, Segment Margin, Waterfall, What-If Budget + Growth scenario
requirements.txt	pandas, matplotlib, seaborn, numpy, openpyxl
README.md	This file
How to Run
pip install -r requirements.txt
python Task4_Financial_Analysis.py
Power BI: import Financial_Sample.xlsx → rename table to Financial → paste measures from Task4_DAX_Measures.txt → create What-If parameters Budget Sales Target and Growth % → build the Waterfall chart with the Waterfall_Step helper.

Recommendations
Fix Enterprise pricing / costs first — COGS above Sales means every Enterprise sale loses money on average.
Cap High discounts — High discount margin (9.07%) is less than half the No-discount margin (21.86%).
Protect Channel Partners + Government — highest margin and highest absolute profit.
Review USA — largest Net Sales but lowest country margin (11.97%).
Live Demo / Dashboard
Task 4 Dashboard — Live Demo (HTML version, same numbers as this README)
Task 4 is part of the Datheon Data Analytics & Power BI Internship.
