# Sales Overview Semantic Model Specification

## 1. Project Overview

This specification defines the functional requirements for a Power BI Sales Performance Analytics solution for Yoda Networks LLC. The project is designed to provide a clear executive-level view of sales performance, budget achievement, and adjusted profitability across geographic areas, industries, and sales personnel.

## 2. Business Objective

Deliver a data-driven dashboard that enables stakeholders to:
- Monitor actual sales performance against budget targets.
- Evaluate fiscal year-to-date performance and compare with prior year.
- Identify high-margin regions, sectors, and sales teams.
- Support rapid decision-making through clear KPIs, trends, and variance analysis.

## 3. Audience

Primary audiences for this report include:
- Executive Management: for top-level KPI monitoring and trend assessment.
- Sales Managers: for performance reviews by area, salesperson, and customer segment.
- Financial Analysts: for variance analysis, budget control, and margin evaluation.

## 4. Key Performance Indicators (KPIs)

### 4.1 Sales (LC)
- Description: Total actual revenue in local currency.
- Business logic: sum of all sales transactions.
- Format: Currency (local currency).
- Required variations:
  - Current period
  - Fiscal year-to-date (YTD)
  - Prior year (PY)
  - Year-over-year growth percentage (YOY %)

### 4.2 Budget Variance (LC & %)
- Description: Difference between actual sales and budgeted sales.
- Business logic:
  - `Budget Variance LC` = `Sales LC - Budget LC`
  - `Budget Variance %` = `(Sales LC / Budget LC) - 1`
- Format: Currency and Percentage.
- Visual guidance: use colored status indicators (green/yellow/red) based on deviation thresholds.

### 4.3 Adjusted Profit %
- Description: Adjusted profit as a percentage of sales.
- Business logic: `Adjusted Profit LC / Sales LC`.
- Format: Percentage.
- Visual guidance: use indicator icons or colored circles to show profitability state.

### 4.4 Additional measures
- `Adjusted Profit LC` — sum of adjusted profit values.
- `Budget Achievement %` — percentage of budget met by actual sales.
- `Average Monthly Sales` — average sales over selected months.
- `Sales Index` — ratio of actual sales to budget.

## 5. Dimensions

### 5.1 Primary dimensions
- `Area`: geographic territory, for example NT, SA, NSW, VIC, QLD, WA, ACT.
- `Industry`: customer industry sector, such as Accommodations, TV-station, or other verticals.
- `Salesperson`: sales consultant or account manager.
- `Date`: fiscal date with year and month hierarchy.
- `Customer`: customer name and segment.
- `Product` (optional): product or item-level detail if available.

### 5.2 Filter dimensions
- Fiscal Year
- Month
- Area
- Industry
- Budget Status or budget state

### 5.3 Dynamic dimension selection
- Page 2 must include a dynamic field parameter allowing users to switch the matrix rows between:
  - Area
  - Industry
  - Salesperson

## 6. Fiscal Calendar Rules

### 6.1 Fiscal year definition
- The fiscal year begins on July 1 and ends on June 30.
- Fiscal year labels should reflect the closing year, for example `FY 2026` for July 1, 2025 through June 30, 2026.

### 6.2 Date hierarchy
- Year
- Quarter
- Month
- Month-Year
- Fiscal Year
- Fiscal Quarter
- Fiscal Month

### 6.3 Time intelligence behavior
- YTD calculations must use the fiscal year boundary of June 30.
- Prior year comparisons must use the corresponding fiscal period in the previous year.

## 7. Required Report Pages

### 7.1 Page 1 — Sales Overview
This page is the executive summary and should include:
- KPI scorecards for key metrics.
- Sales versus budget trend over time.
- Area-level sales and budget comparison.
- Profitability scatter analysis by area.
- Rankings for customer bill, country, salesperson, and industry.

#### Visuals
- KPI cards: Sales YTD, Budget YTD, Budget Variance LC, Sales YOY %, Adjusted Profit % YTD.
- Clustered column chart with target markers for Sales vs Budget over time.
- Clustered column chart by Area showing Sales LC and Budget LC.
- Bubble chart or scatter chart: Adjusted Profit % versus Sales LC by Area.
- Horizontal bar charts for top performers and segments.

### 7.2 Page 2 — Sales Table
This page is the detailed analytical page and should include:
- A matrix with dynamic row grouping by Area, Industry, or Salesperson.
- Measures including Sales, Budget, Variance, Profit, PY, YOY, and conditional formatting.
- Sparklines or trend visuals inside the matrix if supported.

#### Columns and metrics
- Sales LC
- Monthly sales sparkline
- Budget LC
- Budget Variance LC
- Budget Variance %
- Adjusted Profit LC
- Adjusted Profit %
- Sales LC PY
- Sales LC YOY %

### 7.3 Page 3 — Segment Performance (Optional)
This page is optional but recommended for deeper analysis.
- Segment performance by Industry and Area.
- Trend cards for budget achievement and profitability.
- Filters for fiscal year, month, area, and industry.

## 8. Business Rules

### 8.1 Data granularity
- The model must operate at transaction-level grain: one row per sale transaction.
- All aggregation must roll up cleanly through dimensions.

### 8.2 Financial logic
- `Sales LC` is the primary revenue measure.
- `Budget LC` is the target value for the same transaction or aggregated group.
- `Adjusted Profit %` is always calculated relative to `Sales LC`.
- If `Budget LC` is zero, variance percentage calculations must handle division safely without errors.
- If `Sales LC` is zero, profit percentage calculations must return blank or zero cleanly.

### 8.3 Status indicator thresholds
Use thresholds for visual indicators as an implementation guide:
- `Green` when performance is strong or budget is met.
- `Yellow` when performance is near target.
- `Red` when performance is below target by a meaningful margin.

### 8.4 Filtering behavior
- Global filters should apply across all pages.
- The fiscal year filter defaults to the current fiscal year.
- Month filters can allow single or multiple month selection.
- The dynamic dimension selector on the Sales Table page must override only the row hierarchy.

## 9. Validation Scenarios

### 9.1 Schema validation
- Confirm the presence of `Fact_Sales` plus the required dimensions: `Dim_Date`, `Dim_Geography`, `Dim_Staff`, `Dim_Customer`.
- Verify `Fact_Sales` includes keys for `DateKey`, `AreaID`, `SalespersonID`, `CustomerID`, and optional `ProductID`.
- Confirm `Dim_Date` is marked as the active date table.
- Ensure all relationships are one-to-many from dimension to fact.

### 9.2 Measure validation
- `Sales LC YTD` should equal aggregated sales from fiscal year start to the selected date.
- `Sales LC PY` should match the same period one fiscal year earlier.
- `Budget Variance LC` should equal `Sales LC - Budget LC`.
- `Budget Variance %` should calculate safely when `Budget LC = 0`.
- `Adjusted Profit %` should calculate so that zero sales does not produce an error.

### 9.3 Business rule tests
- When `Sales LC` is 1,000 and `Budget LC` is 1,200, `Budget Variance LC` must equal -200 and `Budget Variance %` must equal -16.67%.
- When current fiscal YTD sales are 1,000,000 and prior fiscal YTD sales are 900,000, `Sales LC YOY %` must equal 11.11%.
- When selecting the current fiscal year, YTD values must reset at July 1.

### 9.4 Report behavior tests
- The Sales Overview page should update KPI cards when the fiscal year filter changes.
- The Sales Table page should update row grouping based on the dynamic dimension selection.
- Area and Industry filters should correctly slice all visuals.
- Status indicator colors should reflect budget variance and profit percentage thresholds.

## 10. Notes
- All DAX measure names and comments must be written in English.
- Conditional formatting should use iconography for flags and circles consistent with the report design.
- The final solution should be built in Import Mode with a daily refresh cadence.
