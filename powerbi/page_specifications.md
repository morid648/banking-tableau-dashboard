# Power BI Report Page Specifications & Visual Mapping
## Mitron Bank Strategic Insights Dashboard (Tableau → Power BI Migration)

---

## 1. Global Layout System & Canvas Grid

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│ [Logo] STRATEGIC INSIGHTS DASHBOARD     [Tabs 1-5]                       [i]    │ 0-60px
├────────────┬──────────────────────────────────────────────────────┬─────────────┤
│            │  [KPI 1]            [KPI 2]            [KPI 3]       │             │ 60-180px
│  FILTERS   ├──────────────────────────────────────────────────────┤  CONTEXT /  │
│  (Left     │                                                      │  RIGHT      │
│   Rail,    │               MAIN CONTENT AREA                      │  MAP        │ 180-720px
│   Width    │               (Charts / Treemaps / Tables)           │  PANEL      │
│   180px)   │                                                      │  (Width     │
│            │                                                      │   300px)    │
└────────────┴──────────────────────────────────────────────────────┴─────────────┘
```

- **Canvas Size:** 16:9 Standard (1280 × 720 px)
- **Top Header Bar:** 1280 × 60 px (`#2B2B2B` Charcoal)
- **Left Filter Rail:** 180 × 660 px (`#D2691E` Burnt Sienna)
- **Main Canvas Area:** 800 × 660 px (`#F8F9FA` Light Gray background)
- **Right Panel:** 300 × 660 px (`#FFFFFF` White card background)

---

## 2. Global Filter Panel System (Left Rail)

Synchronized Slicers (Sync Slicers enabled across Pages 1–5):

| # | Slicer Name | Field | Control Type | Default Selection |
|---|---|---|---|---|
| 1 | Month | `Dates[MonthName]` | Dropdown | All |
| 2 | Gender | `dim_customers[gender]` | Dropdown | All |
| 3 | Marital Status | `dim_customers[marital_status]` | Dropdown | All |
| 4 | Age Group | `dim_customers[age_group]` | Dropdown | All |
| 5 | Occupation | `dim_customers[occupation]` | Dropdown | All |
| 6 | Payment Type | `fact_spends[payment_type]` | Dropdown | All |
| 7 | Customer Segment | `dim_customers[customer_segmentation]` | Dropdown | All |
| 8 | City | `dim_customers[city]` | Dropdown | All |
| 9 | Spend Category | `fact_spends[category]` | Dropdown | All |
| 10| Customer ID | `dim_customers[customer_id]` | Dropdown / Search | All |

---

## 3. Page Specifications

### 3.1 Page 1: Demographics (`Demographics`)

* **Header KPIs (Row 1):**
  * Card 1: Total Portfolios (`[active_customers]`, Format: `#,##0`)
  * Card 2: Average Spend (`[average_spends]`, Format: `₹ #,##0.00 M`)
  * Card 3: Average Income (`[average_income]`, Format: `₹ #,##0.00 M`)
* **Main Content (Row 2 - Donut Charts):**
  * Donut 1: Gender Distribution (`dim_customers[gender]`, `[active_customers]`)
  * Donut 2: Marital Status Distribution (`dim_customers[marital_status]`, `[active_customers]`)
  * Donut 3: Customer Segmentation Distribution (`dim_customers[customer_segmentation]`, `[active_customers]`)
* **Main Content (Row 3 - Bar Charts):**
  * Bar 1: Age Group Wise Portfolios (Vertical Column Chart: `dim_customers[age_group]`, `[active_customers]`)
  * Bar 2: Occupation Wise Portfolios (Vertical Column Chart: `dim_customers[occupation]`, `[active_customers]`)
  * Toggle: `Visual Analysis` / `Tabular Analysis` bookmark swapper top-right.
* **Right Panel:**
  * India Map: Customer count by city (Mumbai 1,078, Delhi NCR 768, Bengaluru 717, Chennai 752, Hyderabad 685). Landmark icons annotated.
  * Toggle: `View by Occupation` button.

### 3.2 Page 2: Spend Analysis – 1 (`Spend_Analysis_1`)

* **Header KPIs (Row 1):** Same 3-card header as Page 1.
* **Main Content (Row 2):**
  * Visual 1: Category Spend Treemap (`fact_spends[category]`, `[total_spend]`) — Sized by spend (Bills largest, Groceries 2nd, etc.).
  * Visual 2: Monthly Spend Trend (`Dates[MonthName]` sorted by `month_index`, `[average_spends]`, Area/Line chart).
* **Main Content (Row 3):**
  * Visual 3: Payment Mode Spend (Vertical Bar: `fact_spends[payment_type]`, `[average_spends]`)
  * Visual 4: Occupation Spend (Horizontal Ranked Bar: `dim_customers[occupation]`, `[average_spends]`)
  * Visual 5: Age Group Spend (Donut Chart: `dim_customers[age_group]`, `[average_spends]`)
* **Right Panel:**
  * City Spend Map (`dim_customers[city]`, `[average_spends]`). Custom hover tooltip displaying city spend breakdown by category and occupation.

### 3.3 Page 3: Spend Analysis – 2 (`Spend_Analysis_2`)

* **Header KPIs (Row 1):** Same 3-card header.
* **Main Content:**
  * Spend vs. Income Scatter / Clustered Bar Visual.
  * Parameter Swapper (Field Parameter): Switch view between `Portfolios & Occupation` vs `Payment Mode & Category`.
  * Two-dimensional cross-cut bar visuals (Occupation × Payment Mode, Category × Age Group).

### 3.4 Page 4: Income Analysis (`Income_Analysis`)

* **Header KPIs (Row 1):**
  * Card 1: **Average Income Utilization %** (`[income_utilisation %]`, Format: `0.00%`) — *Metric Swap*
  * Card 2: Average Spend (`[average_spends]`)
  * Card 3: Average Income (`[average_income]`)
* **Main Content:**
  * 3 Utilization Donuts: Gender, Marital Status, Segmentation (showing `[income_utilization]`).
  * Paired Bar Charts: Utilization by Age Group (`[income_utilization]`, 35–45 peak at 46.72%) and Occupation (`[income_utilization]`, Salaried IT peak at 51.04%).
* **Right Panel:**
  * City Income Utilization Map (Mumbai 51.4%, Delhi NCR 48.0%, Bengaluru 43.5%, Hyderabad 36.3%, Chennai 31.1%).

### 3.5 Page 5: Detailed View (`Detailed_View`)

* **Grid Table (Full Width):**
  1. `Customer ID` (`dim_customers[customer_id]`)
  2. `Gender` (`dim_customers[gender]`)
  3. `Marital Status` (`dim_customers[marital_status]`)
  4. `Customer Segmentation` (`dim_customers[customer_segmentation]`)
  5. `Occupation` (`dim_customers[occupation]`)
  6. `Avg Monthly Spend` (`[avg_monthly_spend]`, Currency) — *Corrected label & calc (D2)*
  7. `Total Monthly Income` (`dim_customers[avg_income]`, Currency)
  8. `Avg Income Utilization` (`[income_utilization]`, Data Bar / Gauge formatting)
* **Page-Specific Slicers:**
  * Spend Range Slider (`fact_spends[spend]`)
  * Income Utilization % Slider (`[income_utilization]`)

---

## 4. Parameter & Bookmark Interactivity Definitions

1. **Visual / Tabular Toggle (Demographics):**
   - Bookmark `bm_Demo_Visual`: Shows bar charts, hides data table container.
   - Bookmark `bm_Demo_Tabular`: Hides bar charts, shows detailed summary table container.
2. **Category / Occupation Swapper (Spend-2):**
   - Field Parameter `fp_Spend2_Axis`:
     ```dax
     fp_Spend2_Axis = {
         ("Category", NAMEOF('fact_spends'[category]), 0),
         ("Occupation", NAMEOF('dim_customers'[occupation]), 1)
     }
     ```
3. **Age Group / Occupation Swapper (Income Analysis):**
   - Field Parameter `fp_Income_Demographic`:
     ```dax
     fp_Income_Demographic = {
         ("Age Group", NAMEOF('dim_customers'[age_group]), 0),
         ("Occupation", NAMEOF('dim_customers'[occupation]), 1)
     }
     ```
4. **City Detail Tooltip Page:**
   - Tooltip Canvas (320 × 240 px), Page Name: `tt_City_Detail`.
   - Tooltip fields: `dim_customers[city]`.
   - Micro visuals: Top 3 spend categories in city, Top occupation spend in city.
