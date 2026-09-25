# KPI Validation Scorecard & Regression Results
## Mitron Bank Credit Card Strategic Insights

---

## 1. Validation Scorecard (Python Ground Truth vs Power BI Engine)

All calculations were independently validated using Python 3.13 (`scripts/validate_metrics.py`) against raw CSV data (`dim_customers.csv`, `fact_spends.csv`).

| Metric Name | Python Ground Truth | Shipped Tableau Value | Power BI DAX Value | Status | Absolute Diff |
|---|---|---|---|---|---|
| **Total 6-Month Spend** | ₹ 530,897,755.00 | ₹ 530.90 M | ₹ 530,897,755.00 | **MATCH** | ₹ 0.00 |
| **Avg Monthly Spend** | ₹ 88,482,959.17 | ₹ 88.48 M | ₹ 88,482,959.17 | **MATCH** | < 0.01 M |
| **Avg Monthly Income** | ₹ 206,628,129.00 | ₹ 206.63 M | ₹ 206,628,129.00 | **MATCH** | < 0.01 M |
| **Income Utilization %** | **42.82%** | **42.82%** | **42.82%** | **MATCH** | 0.00% |
| **Active Customer Count** | 4,000 | 4,000 | 4,000 | **MATCH** | 0 |
| **Upper Class Count** | 49 | 49 (1.23%) | 49 | **MATCH** | 0 |
| **Middle Class Count** | 2,242 | 2,242 (56.05%) | 2,242 | **MATCH** | 0 |
| **Lower Class Count** | 1,709 | 1,709 (42.73%) | 1,709 | **MATCH** | 0 |

---

## 2. Demographic Utilization Cut Results

| Cut Dimension | Category / Value | Ground Truth Utilization % | Validation Status |
|---|---|---|---|
| **City** | Mumbai | **51.43%** | PASS |
| **City** | Delhi NCR | **48.03%** | PASS |
| **City** | Bengaluru | **43.46%** | PASS |
| **City** | Hyderabad | **36.25%** | PASS |
| **City** | Chennai | **31.10%** | PASS |
| **Occupation** | Salaried IT Employees | **51.04%** | PASS |
| **Occupation** | Freelancers | **45.80%** | PASS |
| **Occupation** | Salaried Other Employees | **42.10%** | PASS |
| **Occupation** | Business Owners | **33.22%** | PASS |
| **Occupation** | Government Employees | **29.00%** | PASS |
| **Age Group** | 35–45 Years | **46.72%** | PASS |
| **Age Group** | 25–34 Years | **43.66%** | PASS |
| **Age Group** | 21–24 Years | **40.59%** | PASS |
| **Age Group** | 45+ Years | **34.70%** | PASS |

---

## 3. Discrepancy Audit Log & Defect Resolutions

### Finding 1: Customer Segmentation Rule Conflict (D1)
- **Defect Description:** `Banking_power_BI_dax_formulas.xlsx` specified Upper Class as `>64,000`, which resulted in 1,082 customers (27.05%).
- **Verification Method:** Cross-checked against screenshot `assets/01-demographics-tab.png` showing Upper Class = 49 (1.23%).
- **Resolution:** Enforced Tableau formula (`>=80000` Upper, `>=45000` Middle, else Lower) in `powerbi/model_definitions.dax`.

### Finding 2: Detailed View Column Header Mismatch (D2)
- **Defect Description:** The table column was labeled "Total Spend", but customer rows displayed monthly averages.
- **Verification Method:** Reverse-computed Customer ID row (`avg_income` = ₹86,600, displayed spend = ₹26,370). Actual 6-month total is ₹158,222 (÷ 6 = ₹26,370.33).
- **Resolution:** Relabeled header to `Avg Monthly Spend` in Power BI grid visual specification.
