# Semantic Model Design

## 1. Table List
- `Fact_Sales`
- `Dim_Date`
- `Dim_Geography`
- `Dim_Staff`
- `Dim_Customer`
- `Dim_Product` (optional)

## 2. Columns by Table

### `Fact_Sales`
- `TransactionID` — Text
- `DateKey` — Date
- `AreaID` — Text
- `SalespersonID` — Text
- `CustomerID` — Text
- `ProductID` — Text (optional)
- `Sales_LC` — Decimal
- `Budget_LC` — Decimal
- `Profit_LC` — Decimal
- `AdjustedProfit_LC` — Decimal (optional)
- `Budget_Status` — Text (optional)

### `Dim_Date`
- `Date` — Date
- `Year` — Integer
- `Quarter` — Text
- `Month` — Text
- `MonthNumber` — Integer
- `MonthYear` — Text
- `FiscalYear` — Integer
- `FiscalYearLabel` — Text
- `FiscalQuarter` — Text
- `FiscalMonthNumber` — Integer
- `FiscalMonthName` — Text
- `IsCurrentFiscalYear` — Boolean
- `IsCurrentMonth` — Boolean

### `Dim_Geography`
- `AreaID` — Text
- `AreaName` — Text
- `Region` — Text
- `Country` — Text

### `Dim_Staff`
- `SalespersonID` — Text
- `SalespersonName` — Text
- `SalespersonRole` — Text
- `Team` — Text

### `Dim_Customer`
- `CustomerID` — Text
- `CustomerName` — Text
- `IndustryName` — Text
- `CustomerBill` — Text

### `Dim_Product` (optional)
- `ProductID` — Text
- `ProductName` — Text
- `ProductCategory` — Text

## 3. Data Types
- Text: identifiers, names, categories, status fields
- Date: date key and calendar dates
- Integer: year, month number, fiscal year number
- Decimal: currency and profit values
- Boolean: date status flags

## 4. Primary Keys
- `Fact_Sales[TransactionID]`
- `Dim_Date[Date]`
- `Dim_Geography[AreaID]`
- `Dim_Staff[SalespersonID]`
- `Dim_Customer[CustomerID]`
- `Dim_Product[ProductID]` (optional)

## 5. Foreign Keys
- `Fact_Sales[DateKey]` -> `Dim_Date[Date]`
- `Fact_Sales[AreaID]` -> `Dim_Geography[AreaID]`
- `Fact_Sales[SalespersonID]` -> `Dim_Staff[SalespersonID]`
- `Fact_Sales[CustomerID]` -> `Dim_Customer[CustomerID]`
- `Fact_Sales[ProductID]` -> `Dim_Product[ProductID]` (optional)

## 6. Relationships
- `Fact_Sales[DateKey]` to `Dim_Date[Date]`
  - Type: many-to-one
  - Notes: active date relationship for fiscal time intelligence
- `Fact_Sales[AreaID]` to `Dim_Geography[AreaID]`
  - Type: many-to-one
- `Fact_Sales[SalespersonID]` to `Dim_Staff[SalespersonID]`
  - Type: many-to-one
- `Fact_Sales[CustomerID]` to `Dim_Customer[CustomerID]`
  - Type: many-to-one
- `Fact_Sales[ProductID]` to `Dim_Product[ProductID]` (optional)
  - Type: many-to-one

## 7. Required Measures
- `Sales LC`
  - `SUM(Fact_Sales[Sales_LC])`
- `Budget LC`
  - `SUM(Fact_Sales[Budget_LC])`
- `Adjusted Profit LC`
  - `SUM(Fact_Sales[Profit_LC])`
- `Adjusted Profit %`
  - `DIVIDE([Adjusted Profit LC], [Sales LC], 0)`
- `Budget Variance LC`
  - `[Sales LC] - [Budget LC]`
- `Budget Variance %`
  - `DIVIDE([Sales LC] - [Budget LC], [Budget LC], 0)`
- `Sales LC YTD`
  - `TOTALYTD([Sales LC], Dim_Date[Date], "6/30")`
- `Budget LC YTD`
  - `TOTALYTD([Budget LC], Dim_Date[Date], "6/30")`
- `Adjusted Profit LC YTD`
  - `TOTALYTD([Adjusted Profit LC], Dim_Date[Date], "6/30")`
- `Sales LC PY`
  - `CALCULATE([Sales LC], SAMEPERIODLASTYEAR(Dim_Date[Date]))`
- `Sales LC YOY %`
  - `DIVIDE([Sales LC] - [Sales LC PY], ABS([Sales LC PY]), 0)`
- `Budget Achievement %`
  - `DIVIDE([Sales LC], [Budget LC], 0)`
- `Average Monthly Sales`
  - `DIVIDE([Sales LC], DISTINCTCOUNT(Dim_Date[MonthYear]), 0)`
- `Budget Status`
  - Example threshold-based variant for visualization

## Notes
- `Dim_Date` should be configured as the active date table in the model.
- Fiscal year logic is based on July 1 through June 30.
- `Dim_Product` is optional and should only be added if item-level reporting is required.
