import pandas as pd
import sqlite3

# Connect database
conn = sqlite3.connect("bluestock_mf.db")

# =========================
# DIM_FUND
# =========================

perf = pd.read_csv("data/processed/scheme_performance_clean.csv")

dim_fund = perf[
    [
        "amfi_code",
        "scheme_name",
        "fund_house",
        "category",
        "plan"
    ]
].drop_duplicates()

dim_fund.to_sql(
    "dim_fund",
    conn,
    if_exists="replace",
    index=False
)

print("dim_fund created")


# =========================
# DIM_DATE
# =========================

nav = pd.read_csv("data/processed/nav_history_clean.csv")

nav["date"] = pd.to_datetime(nav["date"])

dim_date = pd.DataFrame({
    "date": nav["date"].drop_duplicates().sort_values()
})

dim_date["year"] = dim_date["date"].dt.year
dim_date["month"] = dim_date["date"].dt.month
dim_date["month_name"] = dim_date["date"].dt.month_name()
dim_date["quarter"] = dim_date["date"].dt.quarter

dim_date.to_sql(
    "dim_date",
    conn,
    if_exists="replace",
    index=False
)

print("dim_date created")


# =========================
# FACT_AUM
# =========================

fact_aum = perf[
    [
        "amfi_code",
        "scheme_name",
        "aum_crore"
    ]
]

fact_aum.to_sql(
    "fact_aum",
    conn,
    if_exists="replace",
    index=False
)

print("fact_aum created")

conn.close()

print("\nAll dimension tables created successfully")