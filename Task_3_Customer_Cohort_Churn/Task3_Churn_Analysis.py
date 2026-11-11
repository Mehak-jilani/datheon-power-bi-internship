"""
Datheon Task 3 — Customer Cohort & Churn Analytics
Dataset: IBM Telco Churn (WA_Fn-UseC_-Telco-Customer-Churn.csv)
File: put the CSV in same folder as this script, or change CSV_PATH below.

How to run:
  pip install -r requirements.txt
  python Task3_Churn_Analysis.py

Outputs (in terminal):
  Baseline churn, cohort table, contract / payment / internet / support churn
"""
import pandas as pd
import numpy as np

CSV_PATH = "WA_Fn-UseC_-Telco-Customer-Churn.csv"  # rename your downloaded file to this

def churn_rate(s):
    return round((s == "Yes").mean() * 100, 1)

def main():
    df = pd.read_csv(CSV_PATH, low_memory=False)
    print(f"Shape: {df.shape}  |  Columns: {list(df.columns)}")

    # --- Cleaning ---
    # TotalCharges has 11 blank strings (new customers, tenure = 0). Convert to numeric -> NaN -> fill with 0
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    print(f"TotalCharges blanks: {df['TotalCharges'].isna().sum()} -> filled with 0")
    df["TotalCharges"] = df["TotalCharges"].fillna(0)
    print(f"Duplicates: {df.duplicated().sum()} | Nulls left: {int(df.isna().sum().sum())}")

    # --- 1. Baseline ---
    total = len(df)
    churned = (df["Churn"] == "Yes").sum()
    print(f"\nTotal Customers: {total} | Churned: {churned} | Retained: {total-churned}")
    print(f"Baseline Churn Rate % = {churned}/{total} = {churn_rate(df['Churn'])}%")

    # --- 2. Tenure cohorts (as per Task 3 brief: 0-12, 13-24, ...) ---
    bins = [-1, 12, 24, 36, 48, 60, 72]
    labels = ["0-12", "13-24", "25-36", "37-48", "49-60", "61-72"]
    df["Tenure_Cohort"] = pd.cut(df["tenure"], bins=bins, labels=labels)
    cohort = df.groupby("Tenure_Cohort", observed=True).agg(
        Customers=("Churn", "size"),
        Churned=("Churn", lambda x: (x == "Yes").sum()),
    )
    cohort["Churn_Rate_%"] = df.groupby("Tenure_Cohort", observed=True)["Churn"].apply(churn_rate)
    cohort["Retention_%"] = 100 - cohort["Churn_Rate_%"]
    print("\n--- Tenure Cohort ---")
    print(cohort)

    # --- 3. Contract, Payment, Internet, Support ---
    for col in ["Contract", "PaymentMethod", "InternetService", "TechSupport", "OnlineSecurity", "PaperlessBilling"]:
        print(f"\n--- Churn by {col} ---")
        t = df.groupby(col).agg(Customers=("Churn", "size"), **{"Churn_Rate_%": ("Churn", churn_rate)}).sort_values("Churn_Rate_%", ascending=False)
        print(t)

    # --- 4. High-risk segments (from brief) ---
    print("\n--- High-Risk Segments ---")
    for name, mask in [
        ("Fiber Optic + No TechSupport", (df["InternetService"] == "Fiber optic") & (df["TechSupport"] == "No")),
        ("Month-to-month + No TechSupport", (df["Contract"] == "Month-to-month") & (df["TechSupport"] == "No")),
        ("Month-to-month + Electronic check", (df["Contract"] == "Month-to-month") & (df["PaymentMethod"] == "Electronic check")),
        ("0-12 months + Month-to-month", (df["Tenure_Cohort"] == "0-12") & (df["Contract"] == "Month-to-month")),
    ]:
        print(f"{name}: n={int(mask.sum())}, Churn = {churn_rate(df.loc[mask, 'Churn'])}%")

    # --- 5. Churned vs Retained profile ---
    print("\n--- Churned vs Retained ---")
    print(df.groupby("Churn")[["tenure", "MonthlyCharges", "TotalCharges"]].mean().round(2))

    # --- 6. Cohort x Contract matrix (for heatmap / dashboard) ---
    print("\n--- Cohort x Contract Churn % (heatmap data) ---")
    matrix = df.pivot_table(index="Tenure_Cohort", columns="Contract", values="Churn",
                            aggfunc=lambda x: round((x == "Yes").mean() * 100, 1), observed=True)
    print(matrix)
    print("\nDone. Use these numbers in README + Dashboard.")

if __name__ == "__main__":
    main()
