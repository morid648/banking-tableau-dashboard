# Customer Analytics & Discrepancy Analysis Report
## Mitron Bank Credit Card Strategic Insights

---

## 1. Portfolio Macro Overview

Analyzing 4,000 customer profiles and 864,000 transaction records across a 6-month window (May–October) establishes the macro baseline:

- **Total 6-Month Spend:** ₹ 530,897,755
- **Portfolio Monthly Spend (Avg):** ₹ 88,482,959 (₹ 88.48 M)
- **Portfolio Monthly Income (Sum):** ₹ 206,628,129 (₹ 206.63 M)
- **Portfolio Income Utilization %:** **42.82%**
- **Per-Customer Average Monthly Income:** ₹ 51,657
- **Per-Customer Average Monthly Spend:** ₹ 22,121

---

## 2. Customer Segmentation Analysis

### 2.1 Segment Distribution & Threshold Audit

Using the verified Tableau segmentation rules (`>=80,000` Upper, `>=45,000` Middle, else Lower):

| Segment | Threshold | Customer Count | Portfolio % | Monthly Spend | Monthly Income | Utilization % |
|---|---|---|---|---|---|---|
| **Middle Class** | ₹45,000 – ₹79,999 | 2,242 | 56.05% | ₹ 59.98 M | ₹ 139.38 M | **43.03%** |
| **Lower Class** | < ₹45,000 | 1,709 | 42.73% | ₹ 27.31 M | ₹ 63.21 M | **43.20%** |
| **Upper Class** | ≥ ₹80,000 | 49 | 1.23% | ₹ 1.20 M | ₹ 4.04 M | **29.63%** |

### 2.2 Senior-Level Insight: The Upper Class Utilization Cliff

- While Lower and Middle Class customers utilize ~43% of their monthly income, Upper Class customers display a **sharp drop to 29.63% utilization**.
- *Strategic Read:* This should **not** be interpreted as a poor segment fit. Upper Class customers (`avg_income` ≥ ₹80,000) have significant **untapped disposable capacity**. A premium credit card with high-value travel/luxury perks can capture this unallocated liquidity.

---

## 3. Demographic & Geographic Slicing

### 3.1 Geographic Utilization (City Slicing)

| City | Customer Count | Avg Monthly Spend | Avg Monthly Income | Utilization % | Rank |
|---|---|---|---|---|---|
| **Mumbai** | 1,078 | ₹ 28.67 M | ₹ 55.75 M | **51.43%** | 1 |
| **Delhi NCR** | 768 | ₹ 18.57 M | ₹ 38.68 M | **48.03%** | 2 |
| **Bengaluru** | 717 | ₹ 16.67 M | ₹ 38.36 M | **43.46%** | 3 |
| **Hyderabad** | 685 | ₹ 11.25 M | ₹ 31.04 M | **36.25%** | 4 |
| **Chennai** | 752 | ₹ 13.31 M | ₹ 42.80 M | **31.10%** | 5 |

*Key Read:* Mumbai and Delhi NCR drive portfolio utilization. Chennai displays high income relative to spend, signaling card acquisition growth potential.

### 3.2 Occupation Slicing

| Occupation | Customer Count | Utilization % | Primary Spend Driver |
|---|---|---|---|
| **Salaried IT Employees** | 1,294 | **51.04%** | Bills, Electronics, Travel |
| **Freelancers** | 568 | **45.80%** | Travel, Entertainment, Apparel |
| **Salaried Other Employees** | 1,014 | **42.10%** | Groceries, Bills |
| **Business Owners** | 613 | **33.22%** | Health & Wellness, Electronics |
| **Government Employees** | 511 | **29.00%** | Bills, Groceries |

*Key Read:* IT Professionals and Freelancers are the prime credit card adopters.

### 3.3 Age Group Slicing (Inverted-U Curve)

- **35–45 Years:** **46.72%** Utilization (Peak earning & spending phase)
- **25–34 Years:** **43.66%** Utilization (Career establishment phase)
- **21–24 Years:** **40.59%** Utilization (Entry-level phase)
- **45+ Years:** **34.70%** Utilization (Savings & conservative spending phase)

---

## 4. Spend Category & Payment Type Concentration

- **Top Spend Categories:**
  1. **Bills:** ₹ 104.9 M (6-month total) — Primary recurring expenditure.
  2. **Groceries:** ₹ 87.2 M — Consistent high-frequency baseline.
  3. **Electronics:** ₹ 79.4 M — High transaction value.
  4. **Health & Wellness:** ₹ 65.1 M
  5. **Travel:** ₹ 59.3 M
- **Payment Method Share:**
  1. **Credit Card:** **40.7%** of spend
  2. **UPI:** 26.4%
  3. **Debit Card:** 20.1%
  4. **Net Banking:** 12.8%

---

## 5. Audit of Data & Specification Discrepancies

1. **D1 - Segmentation Threshold Error:**
   The reference DAX spreadsheet defined Upper Class as `>64,000` producing 1,082 customers (27.05%). The shipped dashboard screenshots prove the actual approved threshold is `≥80,000` (49 customers / 1.23%).
2. **D2 - Detailed View Column Mismatch:**
   Reverse computing row 1 (Customer ID with ₹86.6k income, ₹26.37k spend) proved the spend column contains **monthly average spend**, not 6-month cumulative spend. Relabeled to `Avg Monthly Spend`.
