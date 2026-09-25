# Mitron Bank Credit Card Strategy — Final Project Report
## Data-Driven Credit Card Feature Recommendations & Market Positioning

---

## 1. Executive Summary

Mitron Bank is preparing to launch a new credit card line to drive retail banking expansion. Analysis of customer demographic, income, and spending patterns across 4,000 customers and 864,000 transaction records reveals a clear market opportunity: **focusing acquisition on high-utilization urban demographic clusters while creating high-tier incentive structures for untapped high-income segments**.

### Key Portfolio Statistics
- **Monthly Spend Volume:** ₹ 88.48 Million
- **Monthly Income Base:** ₹ 206.63 Million
- **Portfolio Income Utilization %:** **42.82%**
- **Dominant Spend Channels:** Credit Card (40.7%), UPI (26.4%), Debit Card (20.1%)
- **Dominant Categories:** Bills (₹104.9M), Groceries (₹87.2M), Electronics (₹79.4M)

---

## 2. Core Strategic Insights

### 💡 Insight 1: The IT & Urban Professional Powerhouse
- **Data Point:** Salaried IT Employees lead all occupations in income utilization at **51.04%** (₹ 40.62M monthly spend). Mumbai leads all cities at **51.43%** (₹ 28.67M monthly spend).
- **Takeaway:** IT professionals in Tier-1 metros (Mumbai, Delhi NCR, Bengaluru) have high credit confidence, spending heavily on digital transactions, electronics, and utility bills.

### 💡 Insight 2: The Mid-Career Peak (Age 35–45)
- **Data Point:** Customers aged 35–45 display peak utilization at **46.72%** (₹ 31.77M monthly spend), outperforming younger (21–24: 40.59%) and older (45+: 34.70%) cohorts.
- **Takeaway:** This cohort is balancing family lifestyle expenses, electronics upgrades, and utility payments.

### 💡 Insight 3: Unlocking the Upper Class Headroom
- **Data Point:** Upper Class customers (`avg_income` ≥ ₹80,000, 49 customers) show only **29.63% income utilization** compared to ~43% for Lower/Middle Class.
- **Takeaway:** High-income customers possess significant unallocated liquidity. A standard cashback card will fail to engage them; they require a premium rewards and luxury lifestyle proposition.

---

## 3. Product Feature Recommendations

Based on empirical data trends, Mitron Bank should launch **Three Tailored Credit Card Variants**:

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                      MITRON BANK CREDIT CARD PORTFOLIO                          │
├───────────────────────┬─────────────────────────┬───────────────────────────────┤
│  1. MITRON TECH &     │  2. MITRON LIFESTYLE &  │  3. MITRON PRIVÉ              │
│     BILLS ELEVATE     │     FAMILY REWARDS      │     PREMIUM ELITE             │
│  (Target: Salaried IT │  (Target: Age 35-45,    │  (Target: Upper Class /       │
│   & Metro Users)      │   Middle Class)         │   Business Owners)            │
└───────────────────────┴─────────────────────────┴───────────────────────────────┘
```

### Recommendation 1: "Mitron Tech & Bills Elevate Card" (Mass Market / Primary Driver)
- **Target Audience:** Salaried IT Employees (51.04% utilization), Metro residents (Mumbai 51.4%, Delhi 48.0%).
- **Core Features:**
  - **5% Accelerated Cashback** on Utility Bills & Subscriptions (Bills is the #1 spending category at ₹104.9M).
  - **3% Cashback** on Electronics & Gadget purchases (Electronics is #3 category at ₹79.4M).
  - **Zero Annual Fee** with ₹1.5L annual spend waiver.
- **Rationale:** Aligns directly with top transaction categories and high-frequency digital spending.

### Recommendation 2: "Mitron Family & Lifestyle Rewards Card" (Mid-Tier Volume Driver)
- **Target Audience:** Age 35–45 (46.72% utilization), Middle Class segment (56.05% of portfolio).
- **Core Features:**
  - **4% Rewards** on Supermarket & Grocery spends (Groceries is #2 spend category at ₹87.2M).
  - **Complimentary Domestic Airport Lounge Access** (2 per quarter, targeting Travel spend at ₹59.3M).
  - **Fuel Surcharge Waiver** across all fuel stations nationwide.
- **Rationale:** Captures household and family expenses for mid-career earners.

### Recommendation 3: "Mitron Privé Elite Signature Card" (High-Margin Premium Driver)
- **Target Audience:** Upper Class segment (`avg_income` ≥ ₹80,000, 29.63% utilization headroom), Business Owners.
- **Core Features:**
  - **2x Reward Points** on International Travel, Luxury Dining, and Health & Wellness.
  - **Low Foreign Exchange Markup** (1.5% vs. industry standard 3.5%).
  - **Dedicated Concierge Service** & Golf Club Access.
- **Rationale:** Designed to capture the untapped 70%+ unallocated income of high-net-worth customers.

---

## 4. Go-To-Market & Acquisition Strategy

1. **Digital Co-Marketing & Payroll Partnerships:** Partner with IT companies in Mumbai, Bengaluru, and Delhi NCR for direct-to-employee card pre-approvals.
2. **UPI Integration:** Enable RuPay Credit Card link to UPI (capturing the 26.4% UPI market share observed in dataset).
3. **Retention & Anti-Churn:** Provide automated spend-milestone alerts to encourage transition from debit card (20.1% of spends) to credit card.

---

## 5. Risk & Limitations

- **Proxy Metric Nature:** Income Utilization (`spend / income`) is a directional indicator of credit propensity, not a credit risk / default predictor.
- **Static Snapshot:** 6-month historical window (May–October). Continuous monitoring recommended post-launch.
