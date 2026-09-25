"""
Synthetic / Fabricated Data Generator for Mitron Bank Analysis Project
----------------------------------------------------------------------
Generates realistic, schema-compliant synthetic sample datasets for
dim_customers and fact_spends without exposing proprietary/real data,
making the repository safe and lightweight for public GitHub distribution.
"""

import argparse
import itertools
from pathlib import Path
import numpy as np
import pandas as pd

# Canonical Categorical Values
AGE_GROUPS = ['21-24', '25-34', '35-45', '45+']
CITIES = ['Mumbai', 'Delhi NCR', 'Bengaluru', 'Chennai', 'Hyderabad']
OCCUPATIONS = [
    'Salaried IT Employees',
    'Salaried Other Employees',
    'Business Owners',
    'Freelancers',
    'Government Employees'
]
GENDERS = ['Male', 'Female']
MARITAL_STATUSES = ['Married', 'Single']
MONTHS = ['May', 'June', 'July', 'August', 'September', 'October']
CATEGORIES = [
    'Bills',
    'Groceries',
    'Electronics',
    'Health & Wellness',
    'Travel',
    'Food',
    'Entertainment',
    'Apparel',
    'Others'
]
PAYMENT_TYPES = ['Credit Card', 'UPI', 'Debit Card', 'Net Banking']

# Base income priors by occupation (Mean, Std Dev in INR)
OCCUPATION_INCOME_PRIORS = {
    'Salaried IT Employees': (58000, 10000),
    'Business Owners': (64000, 12000),
    'Government Employees': (52000, 8000),
    'Salaried Other Employees': (40000, 7000),
    'Freelancers': (35000, 8000),
}

# Spend category base multipliers relative to average monthly spend
CATEGORY_WEIGHTS = {
    'Bills': 1.8,
    'Groceries': 1.5,
    'Electronics': 1.3,
    'Health & Wellness': 1.0,
    'Travel': 0.9,
    'Food': 0.8,
    'Entertainment': 0.7,
    'Apparel': 0.6,
    'Others': 0.4,
}

PAYMENT_WEIGHTS = {
    'Credit Card': 0.40,
    'UPI': 0.28,
    'Debit Card': 0.20,
    'Net Banking': 0.12,
}


def generate_synthetic_customers(n_customers: int = 50, seed: int = 42) -> pd.DataFrame:
    """Generate synthetic customer demographic profiles."""
    np.random.seed(seed)
    customer_ids = [f"ATQCUS{i+1:04d}" for i in range(n_customers)]

    age_group_probs = [0.15, 0.40, 0.30, 0.15]
    city_probs = [0.30, 0.25, 0.20, 0.15, 0.10]
    occupation_probs = [0.35, 0.25, 0.15, 0.15, 0.10]
    gender_probs = [0.65, 0.35]
    marital_probs = [0.70, 0.30]

    ages = np.random.choice(AGE_GROUPS, size=n_customers, p=age_group_probs)
    cities = np.random.choice(CITIES, size=n_customers, p=city_probs)
    occupations = np.random.choice(OCCUPATIONS, size=n_customers, p=occupation_probs)
    genders = np.random.choice(GENDERS, size=n_customers, p=gender_probs)
    marital_status = np.random.choice(MARITAL_STATUSES, size=n_customers, p=marital_probs)

    incomes = []
    for occ, age in zip(occupations, ages):
        base_mean, base_std = OCCUPATION_INCOME_PRIORS[occ]
        age_bonus = 1.15 if age in ['35-45', '45+'] else 0.85
        income_val = int(np.random.normal(base_mean * age_bonus, base_std))
        income_val = max(24000, min(90000, income_val))
        incomes.append(income_val)

    df_customers = pd.DataFrame({
        'customer_id': customer_ids,
        'age_group': ages,
        'city': cities,
        'occupation': occupations,
        'gender': genders,
        'marital status': marital_status,
        'avg_income': incomes
    })

    return df_customers


def generate_synthetic_spends(df_customers: pd.DataFrame, seed: int = 42) -> pd.DataFrame:
    """
    Generate synthetic spend transactions matching the full combinatorial grain:
    customer_id × month × category × payment_type (216 rows per customer).
    """
    np.random.seed(seed)
    rows = []

    for _, cust in df_customers.iterrows():
        cid = cust['customer_id']
        income = cust['avg_income']
        # Spend capacity scaled around ~35-45% monthly income utilization
        target_monthly_spend = income * np.random.uniform(0.35, 0.48)
        
        # 216 combinations per customer
        for month in MONTHS:
            month_factor = np.random.uniform(0.92, 1.08)
            for cat in CATEGORIES:
                cat_w = CATEGORY_WEIGHTS[cat]
                for ptype in PAYMENT_TYPES:
                    p_w = PAYMENT_WEIGHTS[ptype]
                    
                    # Compute synthetic transaction spend
                    base_amt = (target_monthly_spend / (len(CATEGORIES) * len(PAYMENT_TYPES))) * (cat_w * p_w * 4.0) * month_factor
                    noise = np.random.gamma(shape=2.0, scale=base_amt / 2.0)
                    spend_val = max(15, int(noise + np.random.uniform(5, 50)))
                    
                    rows.append({
                        'customer_id': cid,
                        'month': month,
                        'category': cat,
                        'payment_type': ptype,
                        'spend': spend_val
                    })

    df_spends = pd.DataFrame(rows)
    return df_spends


def main():
    parser = argparse.ArgumentParser(description="Generate fabricated sample banking dataset.")
    parser.add_argument("--customers", type=int, default=50, help="Number of synthetic customers to generate (default: 50).")
    parser.add_argument("--output-dir", type=str, default="Dataset/samples", help="Directory where sample CSVs should be saved.")
    parser.add_argument("--seed", type=int, default=42, help="Random seed for reproducibility.")
    args = parser.parse_args()

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"Generating synthetic dataset with {args.customers} customers (Seed: {args.seed})...")
    df_cust = generate_synthetic_customers(n_customers=args.customers, seed=args.seed)
    df_spends = generate_synthetic_spends(df_cust, seed=args.seed)

    cust_path = out_dir / "dim_customers_sample.csv"
    spends_path = out_dir / "fact_spends_sample.csv"

    df_cust.to_csv(cust_path, index=False)
    df_spends.to_csv(spends_path, index=False)

    print(f"[SUCCESS] Saved {len(df_cust):,} customers to: {cust_path}")
    print(f"[SUCCESS] Saved {len(df_spends):,} spend records to: {spends_path}")
    print(f"Total combinations per customer: {len(df_spends) // len(df_cust)}")


if __name__ == "__main__":
    main()
