# ProjectTest1 Semantic Model Specification

This specification defines functional requirements for a Power BI Sales Performance Analytics solution for ProjectTest1. It provides an executive view of sales, budget, and profitability across areas, industries, and sales staff.

## 1. Project Overview

**Solution Name:** ProjectTest1 Sales Analytics  
**Audience:** Executive Management, Sales Managers, Financial Analysts  
**Primary Use Cases:**
- Monitor actual sales performance against budget targets
- Evaluate fiscal year-to-date (YTD) performance and prior-year comparisons
- Identify high-margin regions and sales teams
- Support rapid decision-making through KPIs, trends, and variance analysis

## 2. Fact Table Definition

### 2.1 Grain

**Primary Fact Table:** `Fact_Sales`

**Grain:** One row per sales transaction at the lowest atomic level (transaction-level detail).

**Grain Definition:**  
Each row in `Fact_Sales` represents:
- One sale transaction
- Identified by `TransactionID` (unique key)
- Associated with a single date, area, salesperson, customer, and product
- Contains measures: `Sales_LC`, `Budget_LC`, and `Profit_LC`

### 2.2 Fact Table Structure

| Column | Type | Description | Key Type |
|--------|------|-------------|----------|
| `TransactionID` | String | Unique transaction identifier | Primary Key |
| `DateKey` | Date | Transaction date (links to Dim_Date) | Foreign Key |
| `AreaID` | String | Geographic area code (links to Dim_Geography) | Foreign Key |
| `SalespersonID` | String | Sales staff identifier (links to Dim_Staff) | Foreign Key |
| `CustomerID` | String | Customer identifier (links to Dim_Customer) | Foreign Key |
| `ProductID` | String | Product identifier (links to Dim_Product) | Foreign Key |
| `Sales_LC` | Double | Actual sales revenue in local currency | Measure |
| `Budget_LC` | Double | Budgeted sales in local currency | Measure |
| `Profit_LC` | Double | Adjusted profit in local currency | Measure |

### 2.3 Aggregation Behavior

All measures aggregate via SUM across dimensions:
- `Total Sales LC = SUM(Sales_LC)` across selected filters
- `Total Budget LC = SUM(Budget_LC)` across selected filters
- `Total Profit LC = SUM(Profit_LC)` across selected filters

## 3. Key Performance Indicators (KPIs)

### 3.1 Sales LC (Local Currency)

**Definition:** Total actual sales revenue in local currency for the selected period.  
**Business Logic:** `SUM(Fact_Sales[Sales_LC])` across selected dimensions.  
**Format:** Currency (local currency)  
**Variations Required:**
- **Current Period:** Sales for the selected date range
- **YTD (Year-to-Date):** Sales from fiscal year start (July 1) to selected date
- **PY (Prior Year):** Sales for the same calendar period in the previous fiscal year
- **YOY %:** Year-over-year growth = `(Sales_YTD - Sales_PY) / Sales_PY`

**Example:** If current YTD sales = 1,000,000 and prior YTD sales = 900,000, then YOY % = 11.11%

### 3.2 Budget LC (Local Currency)

**Definition:** Budgeted sales revenue in local currency for the selected period.  
**Business Logic:** `SUM(Fact_Sales[Budget_LC])` across selected dimensions.  
**Format:** Currency (local currency)

### 3.3 Budget Variance (LC & %)

**Definition:** Difference between actual sales and budgeted sales.  
**Business Logic:**
- `Budget Variance LC = Sales LC - Budget LC`
- `Budget Variance % = (Sales LC / Budget LC) - 1` (with DIVIDE safety if Budget LC = 0)

**Format:** Currency and Percentage  
**Example:** Sales = 1,200, Budget = 1,000 → Variance LC = 200, Variance % = 20%  
**Visual Guidance:** Use color coding (green for favorable, red for unfavorable)

### 3.4 Adjusted Profit LC & %

**Definition:** Adjusted profit in local currency and as a percentage of sales.  
**Business Logic:**
- `Adjusted Profit LC = SUM(Fact_Sales[Profit_LC])`
- `Adjusted Profit % = Adjusted Profit LC / Sales LC` (with DIVIDE safety if Sales LC = 0)

**Format:** Currency and Percentage  
**Example:** Profit = 150,000, Sales = 1,000,000 → Profit % = 15%

### 3.5 Budget Achievement %

**Definition:** Percentage of budget met by actual sales.  
**Business Logic:** `Sales LC / Budget LC` (with DIVIDE safety if Budget LC = 0)  
**Format:** Percentage  
**Example:** Sales = 900, Budget = 1,000 → Budget Achievement = 90%

## 4. Fiscal Calendar Rules

### 4.1 Fiscal Year Definition

- **Fiscal Year Start:** July 1
- **Fiscal Year End:** June 30
- **Fiscal Year Label:** Reflects the closing year (e.g., `FY 2026` = July 1, 2025 through June 30, 2026)

### 4.2 Date Dimension Hierarchy

The `Dim_Date` table must support the following hierarchy:
- **Fiscal Year** (e.g., FY 2026)
- **Fiscal Quarter** (Q1=Jul–Sep, Q2=Oct–Dec, Q3=Jan–Mar, Q4=Apr–Jun)
- **Fiscal Month** (1–12 within fiscal year)
- **Calendar Year** (e.g., 2026)
- **Calendar Quarter** (Q1–Q4 calendar)
- **Calendar Month** (1–12 calendar)
- **Date** (daily grain)
- **Month-Year Label** (e.g., "Jul 2025")

### 4.3 Time Intelligence Behavior

- **YTD Calculations:** Must reset on July 1 (fiscal year boundary), not January 1.
- **Prior Year Comparisons:** Compare fiscal periods; e.g., July 2025 (FY2026 start) compares to July 2024 (FY2025 start).
- **Default Filter:** Fiscal year filter should default to the current fiscal year when no explicit filter is applied.

## 5. Relationship Overview

### 5.1 Star Schema Structure

```
Dim_Date
   |
   | (one-to-many: DateKey)
   |
Fact_Sales ---> Dim_Geography (one-to-many: AreaID)
   |
   +---> Dim_Staff (one-to-many: SalespersonID)
   |
   +---> Dim_Customer (one-to-many: CustomerID)
   |
   +---> Dim_Product (one-to-many: ProductID)
```

### 5.2 Relationship Definitions

| From | To | Foreign Key | Cardinality | Active | Description |
|------|----|----|-------------|--------|-------------|
| `Fact_Sales` | `Dim_Date` | `DateKey` | Many-to-One | Yes | Links transactions to dates |
| `Fact_Sales` | `Dim_Geography` | `AreaID` | Many-to-One | Yes | Links transactions to areas |
| `Fact_Sales` | `Dim_Staff` | `SalespersonID` | Many-to-One | Yes | Links transactions to sales staff |
| `Fact_Sales` | `Dim_Customer` | `CustomerID` | Many-to-One | Yes | Links transactions to customers |
| `Fact_Sales` | `Dim_Product` | `ProductID` | Many-to-One | Yes | Links transactions to products |

### 5.3 Relationship Constraints

- All relationships are one-to-many from dimensions to the fact table.
- `Dim_Date` is the **active date table** for time intelligence.
- All foreign keys in `Fact_Sales` must have matching primary keys in their respective dimension tables.
- No circular relationships or ambiguous paths are permitted.

## 6. Dimensions

| Dimension | Primary Key | Description | Typical Attributes |
|-----------|-------------|-------------|-------------------|
| `Dim_Date` | `DateKey` | Fiscal and calendar dates | Year, Month, Quarter, Fiscal Year, Fiscal Quarter, Fiscal Month |
| `Dim_Geography` | `AreaID` | Geographic areas/territories | Area Code, Area Name, Region |
| `Dim_Staff` | `SalespersonID` | Sales personnel | Salesperson Name, Department, Manager ID |
| `Dim_Customer` | `CustomerID` | Customer entities | Customer Name, Segment, Industry |
| `Dim_Product` | `ProductID` | Product catalog | Product Name, Category, Subcategory |

## 7. Validation Scenarios

### 7.1 Schema Validation
- ✓ Presence of `Fact_Sales` table with all required columns
- ✓ Presence of all dimension tables (`Dim_Date`, `Dim_Geography`, `Dim_Staff`, `Dim_Customer`, `Dim_Product`)
- ✓ All relationships defined and active
- ✓ `Dim_Date` marked as date table

### 7.2 Measure Validation
- ✓ `Sales LC YTD` equals aggregated sales from fiscal year start to selected date
- ✓ `Sales LC PY` matches the same period one fiscal year earlier
- ✓ `Budget Variance LC` = `Sales LC - Budget LC`
- ✓ `Budget Variance %` handles division safely (does not error when Budget LC = 0)
- ✓ `Adjusted Profit %` returns blank or zero when Sales LC = 0 (no errors)

### 7.3 Business Rule Tests
- ✓ When `Sales LC = 1,000` and `Budget LC = 1,200`, then `Budget Variance LC = -200` and `Budget Variance % = -16.67%`
- ✓ When YTD sales = 1,000,000 and prior YTD sales = 900,000, then `Sales YOY % = 11.11%`
- ✓ When fiscal year filter changes, all KPI cards update correctly
- ✓ Fiscal year boundaries reset on July 1 (not January 1)

## 8. Notes

- All DAX measure names and comments must be written in English
- Conditional formatting should use color coding for status (green/yellow/red)
- The solution targets **Import Mode** with daily refresh cadence
- This specification is a scaffold; expand sections as implementation details emerge
