# Mutual Fund Analytics - Data Dictionary

## 1. fact_nav

| Column    | Data Type | Description                   |
| --------- | --------- | ----------------------------- |
| amfi_code | INTEGER   | Unique mutual fund identifier |
| date      | DATE      | NAV date                      |
| nav       | FLOAT     | Net Asset Value of the fund   |

---

## 2. fact_transactions

| Column             | Data Type | Description                     |
| ------------------ | --------- | ------------------------------- |
| investor_id        | TEXT      | Unique investor identifier      |
| transaction_date   | DATE      | Transaction date                |
| amfi_code          | INTEGER   | Mutual fund identifier          |
| transaction_type   | TEXT      | SIP / Lumpsum / Redemption      |
| amount_inr         | FLOAT     | Transaction amount              |
| state              | TEXT      | Investor state                  |
| city               | TEXT      | Investor city                   |
| city_tier          | TEXT      | Tier classification             |
| age_group          | TEXT      | Investor age bucket             |
| gender             | TEXT      | Investor gender                 |
| annual_income_lakh | FLOAT     | Annual income in lakhs          |
| payment_mode       | TEXT      | UPI / Cheque / Net Banking etc. |
| kyc_status         | TEXT      | KYC verification status         |

---

## 3. fact_performance

| Column            | Data Type | Description                     |
| ----------------- | --------- | ------------------------------- |
| amfi_code         | INTEGER   | Mutual fund identifier          |
| scheme_name       | TEXT      | Scheme name                     |
| fund_house        | TEXT      | Fund house                      |
| category          | TEXT      | Fund category                   |
| plan              | TEXT      | Direct / Regular                |
| return_1yr_pct    | FLOAT     | 1-year return percentage        |
| return_3yr_pct    | FLOAT     | 3-year return percentage        |
| return_5yr_pct    | FLOAT     | 5-year return percentage        |
| aum_crore         | FLOAT     | Assets under management (crore) |
| expense_ratio_pct | FLOAT     | Expense ratio percentage        |

---

## 4. dim_fund

| Column      | Data Type | Description      |
| ----------- | --------- | ---------------- |
| amfi_code   | INTEGER   | Primary fund key |
| scheme_name | TEXT      | Scheme name      |
| fund_house  | TEXT      | Fund house       |
| category    | TEXT      | Fund category    |
| plan        | TEXT      | Direct / Regular |

---

## 5. dim_date

| Column     | Data Type | Description    |
| ---------- | --------- | -------------- |
| date       | DATE      | Calendar date  |
| year       | INTEGER   | Year           |
| month      | INTEGER   | Month number   |
| month_name | TEXT      | Month name     |
| quarter    | INTEGER   | Quarter number |

---

## 6. fact_aum

| Column      | Data Type | Description                       |
| ----------- | --------- | --------------------------------- |
| amfi_code   | INTEGER   | Fund identifier                   |
| scheme_name | TEXT      | Scheme name                       |
| aum_crore   | FLOAT     | Assets under management in crores |

---

## Data Sources

| Source File               |
| ------------------------- |
| nav_history.csv           |
| investor_transactions.csv |
| scheme_performance.csv    |

---

## Database

| Database File   |
| --------------- |
| bluestock_mf.db |
