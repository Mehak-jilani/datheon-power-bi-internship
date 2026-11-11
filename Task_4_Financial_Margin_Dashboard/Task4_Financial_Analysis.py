"""
Datheon Task 4 — Corporate Financial & Margin Performance Dashboard
Dataset: Microsoft Financial Sample (Excel) — 700 rows, Sep 2013 to Dec 2014
File: put the Excel in same folder as this script as Financial_Sample.xlsx
       (sheet: Sheet1, columns: Segment, Country, Product, Discount Band,
        Units Sold, Manufacturing Price, Sale Price, Gross Sales, Discounts,
        Sales, COGS, Profit, Date, Month Number, Month Name, Year)

IMPORTANT — Budget / Variance note (read before claiming variance):
  This file has NO Budget / Target column. So true Actual-vs-Budget variance
  CANNOT be computed from the data itself. In Power BI, use the
  What-If Budget Target parameter in Task4_DAX_Measures.txt
  (Budget Sales Target) as the scenario target, and state it as an
  assumption in the README / Dashboard. Do NOT invent a Budget column.

How to run:
  pip install -r requirements.txt
  python Task4_Financial_Analysis.py
Outputs: waterfall inputs, segment / product / country / quarter margins.
"""
import pandas as pd

XLSX = "Financial_Sample.xlsx"

def main():
    df = pd.read_excel(XLSX)
    df.columns = [c.strip() for c in df.columns]
    print(f"Shape: {df.shape} | Columns: {list(df.columns)}")
    df["Discount Band"] = df["Discount Band"].fillna("None")
    print(f"Discount Band blanks filled as 'None': {(df['Discount Band'] == 'None').sum()} rows now None (53 were blank)")
    print(f"Duplicates: {df.duplicated().sum()} | Nulls left: {int(df.isna().sum().sum())}")
    print(f"Date range: {df['Date'].min().date()} to {df['Date'].max().date()}")

    # --- 1. Waterfall: Gross Sales -> Discounts -> Net Sales -> COGS -> Profit ---
    gross = df["Gross Sales"].sum(); disc = df["Discounts"].sum()
    sales = df["Sales"].sum(); cogs = df["COGS"].sum(); profit = df["Profit"].sum()
    print("\n--- WATERFALL (Gross -> Profit) ---")
    print(f"Gross Sales: ${gross:,.2f}")
    print(f"Less: Discounts: -${disc:,.2f} ({disc/gross*100:.2f}% of Gross)")
    print(f"= Net Sales: ${sales:,.2f}")
    print(f"Less: COGS: -${cogs:,.2f} ({cogs/sales*100:.2f}% of Net Sales)")
    print(f"= Profit: ${profit:,.2f} | Margin on Net Sales: {profit/sales*100:.2f}% | COGS Ratio: {cogs/sales*100:.2f}%")
    # sanity: Sales should = Gross - Discounts; Profit should = Sales - COGS
    print(f"Check Sales = Gross-Discounts: {abs(sales-(gross-disc))<0.01} | Check Profit = Sales-COGS: {abs(profit-(sales-cogs))<0.01}")

    # --- 2. Breakdowns ---
    df["Quarter"] = "Q" + ((df["Month Number"]-1)//3+1).astype(str)
    for col in ["Segment", "Product", "Country", "Year", "Quarter", "Discount Band"]:
        t = df.groupby(col).agg(Rows=("Profit","size"), Gross_Sales=("Gross Sales","sum"),
                                Discounts=("Discounts","sum"), Net_Sales=("Sales","sum"),
                                COGS=("COGS","sum"), Profit=("Profit","sum"))
        t["Margin_%"] = (t["Profit"]/t["Net_Sales"]*100).round(2)
        t["COGS_Ratio_%"] = (t["COGS"]/t["Net_Sales"]*100).round(2)
        print(f"\n--- By {col} ---"); print(t.round(2))

    # --- 3. Red flags ---
    print(f"\nNegative-profit rows: {(df['Profit']<0).sum()} / {len(df)}")
    print("Worst 5 rows by Profit:"); print(df.nsmallest(5,"Profit")[["Segment","Country","Product","Discount Band","Sales","COGS","Profit"]])
    print("\nDone. Use these numbers in README + Dashboard. Budget variance uses the What-If parameter, not a data column.")

if __name__ == "__main__":
    main()
