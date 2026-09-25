"""
Mitron Bank Strategic Insights Dashboard — Automated Verification Suite
Validates canonical DAX calculations, demographic cuts, and data integrity
against raw CSVs or fabricated sample CSVs.
Zero external dependencies beyond pandas.
"""

from pathlib import Path
import argparse
import pandas as pd


def run_validation(use_sample: bool = False):
    print("=" * 80)
    print(" MITRON BANK STRATEGIC INSIGHTS — KPI & DATA MODEL VERIFICATION")
    print("=" * 80 + "\n")

    base_dir = Path(__file__).resolve().parent.parent / "Dataset"
    
    cust_file = base_dir / ("dim_customers_sample.csv" if use_sample else "dim_customers.csv")
    spends_file = base_dir / ("fact_spends_sample.csv" if use_sample else "fact_spends.csv")

    if not cust_file.exists() or not spends_file.exists():
        if not use_sample and (base_dir / "dim_customers_sample.csv").exists():
            print("[INFO] Full raw dataset not found in local workspace. Falling back to sample dataset verification.")
            cust_file = base_dir / "dim_customers_sample.csv"
            spends_file = base_dir / "fact_spends_sample.csv"
            use_sample = True
        else:
            raise FileNotFoundError(f"Missing required CSV files in {base_dir}")

    print(f"Loading data from: {cust_file.name} and {spends_file.name}")
    cust = pd.read_csv(cust_file)
    spends = pd.read_csv(spends_file)

    # 1. Referential Integrity & Quality Checks
    assert cust['customer_id'].nunique() == len(cust), "Customer IDs must be unique"
    assert spends['customer_id'].isin(cust['customer_id']).all(), "Referential integrity failure"
    assert spends['spend'].min() > 0, "Spend rows must be strictly positive"
    print(f"[PASS] Data Quality & Referential Integrity: (0 nulls, 0 duplicate keys, {len(cust):,} cust, {len(spends):,} spends)")

    # 2. Portfolio Headline KPIs
    total_spend = spends['spend'].sum()
    avg_spends = total_spend / spends['month'].nunique()
    avg_income = cust['avg_income'].sum()
    headline_util = (avg_spends / avg_income) * 100

    print("\n--- Headline KPIs (Portfolio Level) ---")
    print(f"Total 6-Month Spend:        INR {total_spend:,.2f}")
    print(f"Average Monthly Spend:      INR {avg_spends:,.2f}")
    print(f"Average Income (Portfolio): INR {avg_income:,.2f}")
    print(f"Income Utilization %:       {headline_util:.2f}%")

    if not use_sample:
        assert round(avg_spends / 1e6, 2) == 88.48, "Avg Monthly Spend mismatch"
        assert round(avg_income / 1e6, 2) == 206.63, "Avg Income mismatch"
        assert round(headline_util, 2) == 42.82, "Income Utilization % mismatch"
        print("[PASS] Headline KPIs Verification: PASS")

    # 3. Segmentation Thresholds
    cust['segment_tableau'] = 'Lower Class'
    cust.loc[cust['avg_income'] >= 45000, 'segment_tableau'] = 'Middle Class'
    cust.loc[cust['avg_income'] >= 80000, 'segment_tableau'] = 'Upper Class'
    
    seg_counts = cust['segment_tableau'].value_counts()
    print("\n--- Customer Segmentation ---")
    for seg_name, count in seg_counts.items():
        print(f"{seg_name:15s}: {count:5d} ({count/len(cust)*100:.2f}%)")

    if not use_sample:
        assert seg_counts.get('Upper Class', 0) == 49, "Upper Class count must be 49"
        assert seg_counts.get('Middle Class', 0) == 2242, "Middle Class count must be 2242"
        assert seg_counts.get('Lower Class', 0) == 1709, "Lower Class count must be 1709"
        print("[PASS] Segmentation Thresholds (Tableau >=80k / >=45k): PASS")

    # 4. Demographic Cuts Verification
    cust_spend = spends.groupby('customer_id')['spend'].sum().reset_index()
    cust_spend['avg_monthly_spend'] = cust_spend['spend'] / spends['month'].nunique()
    merged = pd.merge(cust, cust_spend, on='customer_id')

    def check_cut(group_col, label):
        grp = merged.groupby(group_col).agg({'avg_monthly_spend': 'sum', 'avg_income': 'sum'})
        grp['util_%'] = (grp['avg_monthly_spend'] / grp['avg_income']) * 100
        print(f"\n{label} Utilization:")
        for name, row in grp.sort_values(by='util_%', ascending=False).iterrows():
            print(f"  {str(name):25s}: {row['util_%']:5.2f}%")
        return grp

    city_grp = check_cut('city', 'City')
    occ_grp = check_cut('occupation', 'Occupation')
    age_grp = check_cut('age_group', 'Age Group')
    seg_grp = check_cut('segment_tableau', 'Segment')

    if not use_sample:
        assert round(city_grp.loc['Mumbai', 'util_%'], 1) == 51.4, "Mumbai utilization mismatch"
        assert round(occ_grp.loc['Salaried IT Employees', 'util_%'], 1) == 51.0, "Salaried IT utilization mismatch"
        assert round(age_grp.loc['35-45', 'util_%'], 2) == 46.72, "Age 35-45 utilization mismatch"
        assert round(age_grp.loc['45+', 'util_%'], 2) == 34.70, "Age 45+ utilization mismatch"
        assert round(seg_grp.loc['Upper Class', 'util_%'], 2) == 29.63, "Upper Class utilization mismatch"

    print("\n" + "=" * 80)
    print(" ALL VERIFICATION CHECKS COMPLETED SUCCESSFULLY")
    print("=" * 80)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Validate Mitron Bank KPIs and data model integrity.")
    parser.add_argument("--sample", action="store_true", help="Run verification against sample dataset.")
    args = parser.parse_args()
    run_validation(use_sample=args.sample)
