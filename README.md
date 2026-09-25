# Mitron Bank Credit Card Strategy — Tableau → Power BI Migration

[![Power BI](https://img.shields.io/badge/Power_BI-Desktop_&_DAX-F2C811?logo=powerbi&logoColor=black)](https://powerbi.microsoft.com/)
[![Tableau](https://img.shields.io/badge/Tableau-Migration-E97627?logo=tableau&logoColor=white)](https://www.tableau.com/)
[![Python](https://img.shields.io/badge/Python-3.13_Validation-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Data Model](https://img.shields.io/badge/Data_Architecture-Star_Schema-10B981)](#-data-model-architecture--grain-discipline)
[![License](https://img.shields.io/badge/Data_License-codebasics.io_Practice-blue)](#-data-handling--privacy)

An enterprise-grade Business Intelligence migration and customer spend analytics project: migrating an existing Tableau credit-card insights dashboard to Power BI for **Mitron Bank**, independently auditing 864,000 transactions across 4,000 customers, resolving critical upstream specification defects, and architecting an actionable **₹16.88 Cr** credit-card launch strategy.

---

## ⚡ Quick Scan / Executive Snapshot

| Metric / Dimension | Verified Ground Truth Value | Business Context & Strategic Takeaway |
| :--- | :---: | :--- |
| **Total 6-Month Spend** | **₹ 530.90 M** | Cumulative transactions across 8 spend categories (May–Oct 2023). |
| **Avg Monthly Spend** | **₹ 88.48 M / mo** | Baseline portfolio monthly velocity across all payment channels. |
| **Avg Monthly Income** | **₹ 206.63 M / mo** | Total monthly earning capacity across 4,000 active customer profiles. |
| **Income Utilization %** | **42.82%** | Primary behavioral proxy for credit propensity (Spend ÷ Income). |
| **Credit Card Spend Share** | **40.74%** | Dominant payment method (₹216.31M), outperforming UPI (22.5%) and Debit (20.3%). |
| **Top Propensity Metro** | **Mumbai (51.43%)** | Highest utilization metro, followed closely by Delhi NCR (48.03%). |
| **Prime Occupation Cluster**| **Salaried IT (51.04%)**| Highest-volume credit adoption engine with digital payment affinity. |
| **Year-1 Revenue Potential** | **₹ 16.88 Crore** | Projected annual interchange fee income + card membership fees. |
| **Upstream Defects Resolved**| **2 Critical Errors** | Corrected 22x segmentation distortion and mislabeled spend headers. |
| **Automated Test Suite** | **100% PASS** | Zero-dependency Python regression suite validating all calculations. |

---

## 🎯 Business Problem Statement

Mitron Bank, a legacy financial institution headquartered in Hyderabad, is entering the consumer credit card market to expand its retail banking footprint. An exploratory Tableau prototype existed, but the bank needed to:

1. **Migrate to Power BI:** Standardize analytics onto Microsoft 365, improve enterprise governance, and reduce BI licensing costs.
2. **Reconcile Ground Truth & Resolve Upstream Defects:** Raw CSV transactions and reference DAX specifications contained conflicting thresholds and misleading column headers.
3. **Formulate a Data-Backed Card Launch Strategy:** Provide the C-suite with demographic spend segmentation, customer acquisition priorities, card feature packaging, and financial ROI models.

---

## 👥 Key Stakeholders & Target Personas

- **Tony Sharma (Data Department Manager, AtliQ):** Requires 100% mathematical reconciliation between legacy Tableau extracts and Power BI measures, with complete audit logs of logic discrepancies.
- **Mitron Bank Credit Card Strategy Committee:** Needs actionable demographic targeting (Metros, Age, Occupation) and customer spend propensity drivers.
- **Chief Commercial Officer (CCO) & Retail Leadership:** Requires commercial sensitivity models, annual revenue projections, and unit economics for product launch sign-off.

---

## 🔍 Upstream Quality Assurance: 2 Critical Defects Resolved

A senior analyst audits specifications rather than assuming upstream files are infallible. Independent Python verification surfaced two major errors in the provided project material:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ DISCREPANCY 1: Customer Segmentation Rule Defect (22x Error Averted)                  │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ • Defective Spec (Excel):  Upper Class defined as avg_income > ₹64,000                 │
│                            Yields: 1,082 Upper Class customers (27.05% of portfolio)  │
│ • Ground Truth (Verified): Shipped Tableau dashboard confirmed strictly 49 customers   │
│                            Correct threshold: avg_income >= ₹80,000 (1.23% of total)   │
│ • Strategic Impact:        Adopting spec blindly would have caused a 2,200% error in   │
│                            affluent marketing spend and card benefit liability!        │
└────────────────────────────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────────────────────────────┐
│ DISCREPANCY 2: Detailed View Column Header Label Mismatch                              │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ • Defective Header:        Column labeled "Total Spend" showed ₹26,370 for an          │
│                            ₹86,600/mo income customer whose 6-month spend was ₹158,222.│
│ • Mathematical Proof:      ₹158,222 cumulative ÷ 6 months = ₹26,370.33 average/month.  │
│ • Resolution:              Metric was monthly average, but label claimed total spend.   │
│                            Correctly relabeled to "Avg Monthly Spend" in Power BI.      │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Data Model Architecture & Grain Discipline

The Power BI data model adheres strictly to the **Ralph Kimball Star Schema** standard, guaranteeing lightning-fast VertiPaq compression and zero risk of fan-out double-counting:

```
       ┌────────────────────────┐                   ┌────────────────────────┐
       │     dim_customers      │                   │         Dates          │
       ├────────────────────────┤                   ├────────────────────────┤
       │ PK  customer_id        │                   │ PK  MonthName          │
       │     gender             │                   │     month_index (Sort) │
       │     age_group          │                   │     Quarter            │
       │     marital_status     │                   └───────────┬────────────┘
       │     city               │                               │
       │     occupation         │                               │ 1
       │     avg_income         │                               │
       │     customer_segment   │                               │ Single Filter
       └───────────┬────────────┘                               │
                   │ 1                                          │
                   │                                            │
                   │ Single Direction                           │
                   │                                            ▼ *
                   │                                ┌────────────────────────┐
                   └───────────────────────────────►│      fact_spends       │
                                                  * ├────────────────────────┤
                                                    │ FK  customer_id        │
                                                    │ FK  month              │
                                                    │     category           │
                                                    │     payment_type       │
                                                    │     spend (Base)       │
                                                    └────────────────────────┘
```

### Key Architectural Specifications:
- **Composite Fact Grain:** `fact_spends` is recorded at the unique grain of `customer_id × month × category × payment_type` across **864,000 records**.
- **Pure Single-Direction Relationships (`1 : *`):** Dimensions filter facts cleanly. Zero bidirectional traps, eliminating ambiguous filter paths and inflated aggregations.
- **Chronological Calendar Architecture:** Solves the Power BI alphabetical sorting trap (`August → July → June → May...`) by linking `Dates[MonthName]` to a dedicated `Dates[month_index]` numeric column (5 for May to 10 for October).

---

## 📊 Core Analytical Findings

### 1. Metro Geographic Propensity (Spend ÷ Income)
- **Mumbai (51.43%)** and **Delhi NCR (48.03%)** are the undisputed Tier-1 volume drivers.
- **Bengaluru (43.46%)** represents high electronics and dining velocity.
- **Hyderabad (36.25%)** and **Chennai (31.10%)** present lower initial utilization but significant headroom for regional branch expansion.

### 2. The Mid-Career Inverted-U Peak (Age 35–45)
- Utilization forms an inverted-U curve: **21–24 (40.59%)** → **25–34 (43.66%)** → **35–45 (46.72% Peak)** → **45+ (34.70%)**.
- Customers aged 35–45 manage major household outlays (Groceries, Electronics, Health, Utilities) with stable, high repayment reliability.

### 3. The Upper-Class Utilization Cliff & Liquidity Headroom
- Lower Class (**43.20%**) and Middle Class (**43.03%**) spend heavily on day-to-day essentials.
- Upper Class (**avg_income ≥ ₹80,000**) utilization drops sharply to **29.63%** — leaving **70.37% unallocated monthly income**.
- **Untapped Liquidity:** Affluent customers earn an average ₹82,400/month but spend only ₹24,418 on primary channels, leaving **₹2.84 Million / month** in untapped credit capacity per cohort.
- **The Cashback Fallacy:** Affluent customers do not optimize for 1% grocery cashback; they demand travel concierge, international lounge privileges, and zero-forex markups.

---

## 💳 Product Strategy & Commercial Impact

Based on customer spend clustering, we designed a **3-tier product portfolio** coupled with an interactive financial sensitivity engine:

### 1. Tailored Credit Card Portfolio

| Card Variant | Target Segment | Key Value Proposition & Benefits | Fee Architecture |
| :--- | :--- | :--- | :--- |
| **Mitron Tech & Bills Elevate** *(Volume Driver)* | Salaried IT & Metros (51.04% Util) | • 5% Cashback on Utility Bills & Subscriptions<br>• 3% on Electronics & Gadget Retail<br>• 1% Universal Flat Cashback | ₹999 / yr<br>*(Waived at ₹1.5L spend)* |
| **Mitron Family & Lifestyle Rewards** *(Lifestyle Driver)* | Age 35–45 & Middle Class (46.72% Util) | • 4% Accelerated Grocery Rewards<br>• 2 Domestic Lounge Visits / Quarter<br>• 1.5% Fuel Surcharge Waiver | ₹1,499 / yr<br>*(Waived at ₹2.5L spend)* |
| **Mitron Privé Elite Signature** *(High-Margin Premium)* | Upper Class Affluent (29.63% Util) | • 2x Points on Luxury & International Travel<br>• Low 1.5% Forex Markup (vs. 3.5% industry)<br>• 24/7 Dedicated Concierge & Golf Access | ₹4,999 / yr<br>*(Complimentary ₹1 Cr Travel Insurance)* |

### 2. Year-1 Portfolio Revenue Projection Model

$$\text{Total Annual Revenue} = (\text{Active Cardholders} \times \text{Avg Monthly Spend} \times 12 \times \text{Interchange \%}) + (\text{Active Cardholders} \times \text{Annual Fee})$$

- **Baseline Assumptions:** 2,500 active cardholders • ₹25,000 avg monthly spend • 1.75% blended net interchange fee • ₹1,500 blended annual fee.
- **Year-1 Projected Revenue:** **₹ 16.88 Crore**
  - **Interchange Income:** ₹ 13.13 Cr *(77.8%)*
  - **Annual Membership Fees:** ₹ 3.75 Cr *(22.2%)*
- **Sensitivity:** Every ₹2,500 lift in average monthly spend generates an additional **₹ 1.31 Crore** in net interchange income with zero customer acquisition cost.

---

## 🖥️ Power BI Report Pages

The migrated Power BI solution comprises 5 interactive analytical pages:

1. **Demographics Page:** Executive KPI ribbon, demographic distribution by Gender, Marital Status, Age Group, Occupation, and dynamic City map.
2. **Spend Analysis — 1 Page:** Category treemaps (Bills ₹104.9M, Groceries ₹87.2M), monthly trend, payment mode breakdown, and ranked occupation bars.
3. **Spend Analysis — 2 Page:** Category vs. Occupation matrix, spend-to-income distribution visuals, and interactive parameter swappers.
4. **Income Analysis Page:** **Headline KPI Swap to Avg Income Utilization %**, utilization donuts, age band curves, and metro utilization rankings.
5. **Detailed View Page:** Granular tabular audit grid with corrected `Avg Monthly Spend` column and dynamic multi-criteria slicers.

---

## 🗂️ Clean Repository Architecture

```
├── README.md                                 ← You are here: Recruiter-friendly Executive Summary
├── Dataset/                                  ← Schema, data dictionaries & fabricated samples
│   ├── samples/                              ← Pre-generated synthetic sample datasets
│   │   ├── dim_customers_sample.csv          ← 50 synthetic customer profiles
│   │   └── fact_spends_sample.csv            ← 10,800 synthetic spend records
│   ├── dim_customers_sample.csv              ← Root sample customer profile CSV
│   ├── fact_spends_sample.csv                ← Root sample spend transactions CSV
│   ├── meta_data.txt                         ← Source data dictionary & schema
│   └── README.md                             ← Dataset documentation & fabrication instructions
├── tableau/                                  ← Legacy source Tableau workbook & specs
│   ├── Banking Strategic Dashboard.twbx      ← Original source Tableau packaged workbook
│   └── Tableau Banking Dashboard - Supplement Document.xlsx
├── powerbi/                                  ← Power BI migration artifacts & models
│   ├── Banking_power_BI_dax_formulas.xlsx    ← Reference spec formula sheet (audited)
│   ├── power_query_setup.m                   ← Power Query M ETL & Dates table script
│   ├── model_definitions.dax                 ← Canonical DAX measures & calculated columns
│   ├── theme_mitron.json                     ← Custom Power BI theme JSON
│   └── page_specifications.md                ← Visual placement & canvas grid specs
├── presentation/                             ← Executive slide decks
│   ├── Mitron_Bank_Executive_Strategy.pptx   ← 9-slide CXO Executive Deck (widescreen 16:9 + speaker notes)
│   └── Banking_project_supplements_ppt.pptx  ← Project briefing presentation supplement
├── docs/                                     ← In-depth analytical documentation
│   ├── ANALYSIS.md                           ← In-depth customer segmentation & spend analysis
│   ├── RESULTS.md                            ← Validation scorecard & KPI comparison diffs
│   └── PROJECT_REPORT.md                     ← Final executive report & recommendations
├── scripts/
│   ├── fabricate_sample_data.py              ← Synthetic data fabrication generator
│   └── validate_metrics.py                   ← Python regression test suite (100% PASS, zero external deps)
└── assets/                                   ← High-resolution visual screenshots & walkthrough GIF
    ├── 01-demographics-tab.png
    ├── 02-spend-analysis-tab.png
    ├── 03-income-analysis-tab.png
    ├── 04-data-model.png
    ├── 05-presentation-executive-summary.png
    ├── 06-presentation-defect-audit.png
    ├── 07-presentation-card-strategy-roi.png
    ├── 08-star-schema-studio.png
    └── dashboard-demo.gif
```

---

## ⚡ Automated Test Suite Execution

Validate all DAX calculations, demographic cuts, and data model integrity directly via Python (supports both full datasets and sample datasets):

```bash
# Validate against local full dataset (if present):
python scripts/validate_metrics.py

# Validate against synthetic sample dataset:
python scripts/validate_metrics.py --sample

# Fabricate fresh synthetic data of custom size:
python scripts/fabricate_sample_data.py --customers 100 --output-dir Dataset/samples
```

---

## 🔒 Data Handling & Public Distribution

- In accordance with data privacy and public repository best practices, large raw production datasets are omitted via `.gitignore`.
- Pre-packaged **fabricated sample datasets** (`dim_customers_sample.csv`, `fact_spends_sample.csv`) and the automated generator script (`scripts/fabricate_sample_data.py`) are provided for testing, code review, and full reproducibility.
- All DAX code, Power Query scripts, theme definitions, presentation decks, and analytical documentation are original open-source deliverables.

---
**Built by :**
- [Anshul](https://github.com/morid648) 
- [LinkedIn](https://www.linkedin.com/in/anshul-chaudhary-508138308/)
