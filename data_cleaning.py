import pandas as pd
import os

os.makedirs("data/processed", exist_ok=True)

# NAV HISTORY

nav = pd.read_csv("data/raw/Copy of 02_nav_history.csv")

nav["date"] = pd.to_datetime(nav["date"])

nav = nav.sort_values(["amfi_code", "date"])

nav = nav.drop_duplicates()

nav = nav[nav["nav"] > 0]

nav.to_csv(
    "data/processed/nav_history_clean.csv",
    index=False
)

print("NAV cleaned")

# INVESTOR TRANSACTIONS

txn = pd.read_csv(
    "data/raw/Copy of 08_investor_transactions.csv"
)

txn["transaction_date"] = pd.to_datetime(
    txn["transaction_date"]
)

txn["transaction_type"] = (
    txn["transaction_type"]
    .str.strip()
    .str.title()
)

valid_types = [
    "Sip",
    "Lumpsum",
    "Redemption"
]

txn = txn[
    txn["transaction_type"].isin(valid_types)
]

txn = txn[
    txn["amount_inr"] > 0
]

valid_kyc = [
    "Verified",
    "Pending"
]

txn = txn[
    txn["kyc_status"].isin(valid_kyc)
]

txn.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index=False
)

print("Transactions cleaned")

# SCHEME PERFORMANCE

perf = pd.read_csv(
    "data/raw/Copy of 07_scheme_performance.csv"
)

return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_cols:
    perf[col] = pd.to_numeric(
        perf[col],
        errors="coerce"
    )

perf = perf.dropna(
    subset=return_cols
)

perf["expense_flag"] = (
    (perf["expense_ratio_pct"] < 0.1)
    |
    (perf["expense_ratio_pct"] > 2.5)
)

perf.to_csv(
    "data/processed/scheme_performance_clean.csv",
    index=False
)

print("Performance cleaned")

print("\nDone")