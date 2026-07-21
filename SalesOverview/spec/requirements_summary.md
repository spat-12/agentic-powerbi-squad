# Sales Overview Requirements Summary

## 1. Business Goals
- Provide executives with a concise view of sales performance, budget achievement, and profitability.
- Enable sales managers to assess performance by area, industry, and salesperson.
- Enable financial analysts to analyze budget variance and year-over-year trends.
- Support fast decision-making through clear KPI reporting and trend analysis.

## 2. KPI Definitions
- **Sales (LC):** Total actual revenue in local currency.
  - Variations: current period, fiscal year-to-date (YTD), prior year (PY), year-over-year growth percentage (YOY %).
- **Budget Variance (LC & %):** Difference between actual sales and budgeted sales.
  - `Budget Variance LC` = `Sales LC - Budget LC`
  - `Budget Variance %` = `(Sales LC / Budget LC) - 1`
- **Adjusted Profit %:** Adjusted profit divided by actual sales.
  - `Adjusted Profit %` = `Adjusted Profit LC / Sales LC`
- **Adjusted Profit LC:** Sum of adjusted profit values.
- **Budget Achievement %:** Percentage of budget met by actual sales.
- **Average Monthly Sales:** Average sales over selected months.
- **Sales Index:** Ratio of actual sales to budget.

## 3. Dimensions
- `Area` — geographic territory such as NT, SA, NSW, VIC, QLD, WA, ACT.
- `Industry` — customer industry sector such as Accommodations or TV-station.
- `Salesperson` — sales consultant or account manager.
- `Date` — fiscal date with year and month hierarchy.
- `Customer` — customer name and segment.
- `Product` (optional) — item or product detail if available.
- Filter dimensions:
  - Fiscal Year
  - Month
  - Area
  - Industry
  - Budget Status

## 4. Fact Table Grain
- The fact table must be transaction-level.
- Each row represents a single sales transaction.
- The transaction fact should include sales amount, budget amount, adjusted profit, and foreign keys to date, geography, salesperson, customer, and optionally product.

## 5. Business Constraints
- Fiscal year starts July 1 and ends June 30.
- Fiscal year labels use the closing year (for example `FY 2026` for July 1, 2025 to June 30, 2026).
- YTD calculations must use the July 1 to June 30 fiscal boundary.
- Prior year comparisons must use the corresponding fiscal period from the previous year.
- `Budget Variance %` and `Adjusted Profit %` must handle zero denominators safely.
- Global filters must apply consistently across report pages.
- The report should be built in Import Mode with daily refresh cadence.

## 6. Assumptions
- No row-level security is required; all users can see the full dataset.
- Budget values are available at the same granularity as sales transactions or can be aggregated consistently.
- Adjusted profit is either stored directly or can be calculated reliably from available financial fields.
- The model can support a dynamic row-level selector for Area, Industry, and Salesperson on the detailed matrix page.
- Visual indicators will use green/yellow/red thresholds for budget and profit status.

## 7. Implementation Notes
- Use `Dim_Date` as the active date table for time intelligence.
- Implement fiscal YTD and prior year calculations using the June 30 fiscal year-end boundary.
- Build an executive overview page with KPI cards, trend charts, area comparisons, and ranking visuals.
- Build a detailed matrix page with dynamic row grouping and conditional formatting.
- Optionally add a segment performance page for deeper analysis by industry and area.
- Keep DAX measure names and comments in English.
- Ensure the dynamic dimension selector affects only row grouping on the sales table page.
- Use iconography for flags and circles to represent budget variance and profit state.
