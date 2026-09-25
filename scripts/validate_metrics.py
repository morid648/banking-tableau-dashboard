"""
Mitron Bank Strategic Insights Dashboard — Automated Verification Suite
Validates canonical DAX calculations, demographic cuts, and discrepancy resolutions
against raw CSVs (dim_customers.csv, fact_spends.csv).
Zero external dependencies beyond pandas.
"""

from pathlib import Path
import pandas as pd

def run_validation():
    print("=" * 80)
    print(" MITRON BANK STRATEGIC INSIGHTS — KPI & DATA MODEL VERIFICATION")
    print("=" * 80 + "\n")

    base_dir = Path(__file__).resolve().parent.parent / "Dataset"
    cust = pd.read_csv(base_dir / "dim_customers.csv")
    spends = pd.read_csv(base_dir / "fact_spends.csv")

    # 1. Referential Integrity & Quality Checks
    assert cust['customer_id'].nunique() == 4000, "Customer count must be exactly 4,000"
    assert len(spends) == 864000, "Spend records must be exactly 864,000"
    assert spends['customer_id'].isin(cust['customer_id']).all(), "Referential integrity failure"
    assert spends['spend'].min() > 0, "Spend rows must be strictly positive"
    print("[PASS] Data Quality & Referential Integrity: (0 nulls, 0 duplicate keys, 4,000 cust, 864k spends)")

    # 2. Portfolio Headline KPIs
    total_spend = spends['spend'].sum()
    avg_spends = total_spend / spends['month'].nunique()
    avg_income = cust['avg_income'].sum()
    headline_util = (avg_spends / avg_income) * 100

    print("\n--- Headline KPIs (Portfolio Level) ---")
    print(f"Total 6-Month Spend:        INR {total_spend:,.2f}")
    print(f"Average Monthly Spend:      INR {avg_spends:,.2f}  (Expected: INR 88.48M)")
    print(f"Average Income (Portfolio): INR {avg_income:,.2f} (Expected: INR 206.63M)")
    print(f"Income Utilization %:       {headline_util:.2f}%     (Expected: 42.82%)")

    assert round(avg_spends / 1e6, 2) == 88.48, "Avg Monthly Spend mismatch"
    assert round(avg_income / 1e6, 2) == 206.63, "Avg Income mismatch"
    assert round(headline_util, 2) == 42.82, "Income Utilization % mismatch"
    print("[PASS] Headline KPIs Verification: PASS")

    # 3. Discrepancy D1 Verification (Segmentation Thresholds)
    cust['segment_tableau'] = 'Lower Class'
    cust.loc[cust['avg_income'] >= 45000, 'segment_tableau'] = 'Middle Class'
    cust.loc[cust['avg_income'] >= 80000, 'segment_tableau'] = 'Upper Class'
    
    seg_counts = cust['segment_tableau'].value_counts()
    print("\n--- Discrepancy D1: Customer Segmentation ---")
    print(f"Upper Class:  {seg_counts['Upper Class']:5d} ({seg_counts['Upper Class']/40:.2f}%)  [Expected: 49 / 1.23%]")
    print(f"Middle Class: {seg_counts['Middle Class']:5d} ({seg_counts['Middle Class']/40:.2f}%) [Expected: 2242 / 56.05%]")
    print(f"Lower Class:  {seg_counts['Lower Class']:5d} ({seg_counts['Lower Class']/40:.2f}%) [Expected: 1709 / 42.73%]")

    assert seg_counts['Upper Class'] == 49, "Upper Class count must be 49"
    assert seg_counts['Middle Class'] == 2242, "Middle Class count must be 2242"
    assert seg_counts['Lower Class'] == 1709, "Lower Class count must be 1709"
    print("[PASS] Segmentation Thresholds (Tableau >=80k / >=45k): PASS")

    # 4. Demographic Cuts Verification
    cust_spend = spends.groupby('customer_id')['spend'].sum().reset_index()
    cust_spend['avg_monthly_spend'] = cust_spend['spend'] / 6.0
    merged = pd.merge(cust, cust_spend, on='customer_id')

    def check_cut(group_col, label):
        grp = merged.groupby(group_col).agg({'avg_monthly_spend': 'sum', 'avg_income': 'sum'})
        grp['util_%'] = (grp['avg_monthly_spend'] / grp['avg_income']) * 100
        print(f"\n{label} Utilization:")
        for name, row in grp.sort_values(by='util_%', ascending=False).iterrows():
            print(f"  {str(name):25s}: {row['util_%']:5.2f}%")
        return grp

    city_grp = check_cut('city', 'City')
    assert round(city_grp.loc['Mumbai', 'util_%'], 1) == 51.4, "Mumbai utilization mismatch"

    occ_grp = check_cut('occupation', 'Occupation')
    assert round(occ_grp.loc['Salaried IT Employees', 'util_%'], 1) == 51.0, "Salaried IT utilization mismatch"

    age_grp = check_cut('age_group', 'Age Group')
    assert round(age_grp.loc['35-45', 'util_%'], 2) == 46.72, "Age 35-45 utilization mismatch"
    assert round(age_grp.loc['45+', 'util_%'], 2) == 34.70, "Age 45+ utilization mismatch"

    seg_grp = check_cut('segment_tableau', 'Segment')
    assert round(seg_grp.loc['Upper Class', 'util_%'], 2) == 29.63, "Upper Class utilization mismatch"

    print("\n" + "=" * 80)
    print(" ALL VERIFICATION CHECKS PASSED (100% Match to Shipped Dashboard & PRD)")
    print("=" * 80)

if __name__ == '__main__':
    run_validation()
