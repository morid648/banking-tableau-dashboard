# 📊 Dataset Information & Public Distribution Notice

> [!NOTE]
> **Data Privacy & GitHub Best Practices:**  
> In compliance with data sharing guidelines and repository size best practices for public GitHub repositories, the original raw 36MB dataset (`fact_spends.csv` with 864,000 records) is omitted via `.gitignore`. A high-fidelity, schema-identical **fabricated sample dataset** is provided for review, testing, and portfolio demonstration.

---

## 📁 Included Sample Datasets

The repository includes pre-generated synthetic sample data matching the exact schema, data types, and combinatorial structure of the project:

- **`dim_customers_sample.csv`** (and `samples/dim_customers_sample.csv`):
  - 50 synthetic demographic customer profiles.
  - Columns: `customer_id`, `age_group`, `city`, `occupation`, `gender`, `marital status`, `avg_income`.
- **`fact_spends_sample.csv`** (and `samples/fact_spends_sample.csv`):
  - 10,800 synthetic spend transactions across all 6 months (May–October), 9 spending categories, and 4 payment modes ($50 \times 216 = 10,800$ rows).
  - Columns: `customer_id`, `month`, `category`, `payment_type`, `spend`.
- **`meta_data.txt`**:
  - Full schema and column definitions.

---

## ⚙️ Generating Synthetic / Fabricated Data

To fabricate a synthetic dataset of any arbitrary size (e.g. 50, 500, or 4,000 customers), run the included Python data generator:

```bash
# Generate sample dataset (50 customers, 10.8k transactions)
python scripts/fabricate_sample_data.py --customers 50 --output-dir Dataset/samples

# Generate full-scale synthetic dataset (4,000 customers, 864k transactions)
python scripts/fabricate_sample_data.py --customers 4000 --output-dir Dataset
```

### Generator Parameters:
- `--customers`: Number of unique customer profiles to generate (default: `50`).
- `--output-dir`: Output directory path (default: `Dataset/samples`).
- `--seed`: Random seed for deterministic reproducibility (default: `42`).
