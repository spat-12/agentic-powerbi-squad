# Sales Overview ER Diagram

## Star Schema Overview
This model uses a star schema with a single fact table and multiple dimensions. The fact table stores transaction-level sales metrics, and each dimension provides contextual attributes for slicing and filtering.

## Fact Table
- **Fact_Sales**
  - Grain: one row per sales transaction.
  - Purpose: store sales, budget, and adjusted profit values connected to date, geography, salesperson, and customer.

## Dimension Tables
- **Dim_Date**
  - Attributes: Date, Year, Quarter, Month, Month-Year, Fiscal Year, Fiscal Quarter, Fiscal Month.
- **Dim_Geography**
  - Attributes: AreaID, AreaName, Region, Country.
- **Dim_Staff**
  - Attributes: SalespersonID, SalespersonName, Role, Team.
- **Dim_Customer**
  - Attributes: CustomerID, CustomerName, IndustryName, CustomerBill.
- **Dim_Product** (optional)
  - Attributes: ProductID, ProductName, ProductCategory.

## Keys
- Fact table key: `Fact_Sales[TransactionID]` (transaction-level unique identifier).
- Foreign keys:
  - `Fact_Sales[DateKey]`
  - `Fact_Sales[AreaID]`
  - `Fact_Sales[SalespersonID]`
  - `Fact_Sales[CustomerID]`
  - `Fact_Sales[ProductID]` (optional)
- Dimension primary keys:
  - `Dim_Date[Date]`
  - `Dim_Geography[AreaID]`
  - `Dim_Staff[SalespersonID]`
  - `Dim_Customer[CustomerID]`
  - `Dim_Product[ProductID]`

## Relationships and Cardinality
- Fact_Sales[DateKey] -> Dim_Date[Date]
  - Cardinality: Many (fact) to One (date)
  - Active date relationship used for time intelligence.
- Fact_Sales[AreaID] -> Dim_Geography[AreaID]
  - Cardinality: Many to One
- Fact_Sales[SalespersonID] -> Dim_Staff[SalespersonID]
  - Cardinality: Many to One
- Fact_Sales[CustomerID] -> Dim_Customer[CustomerID]
  - Cardinality: Many to One
- Fact_Sales[ProductID] -> Dim_Product[ProductID] (if present)
  - Cardinality: Many to One

## Text-based ER Diagram
```text
               Dim_Date
                 [Date]
                   ^
                   |
                   |
  Dim_Geography   |   Dim_Staff    Dim_Customer    Dim_Product
    [AreaID]      |    [SalespersonID]   [CustomerID]   [ProductID]
        \         |         |              |             |
         \        |         |              |             |
          \       |         |              |             |
           +------>+---------+--------------+-------------+
                    |                                   |
                    |      Fact_Sales                   |
                    |  [TransactionID]                  |
                    |  [DateKey]                        |
                    |  [AreaID]                         |
                    |  [SalespersonID]                  |
                    |  [CustomerID]                     |
                    |  [ProductID] (optional)           |
                    |  [Sales_LC]                        |
                    |  [Budget_LC]                       |
                    |  [Profit_LC]                       |
                    +-----------------------------------+
```

## Grain
- Each row in `Fact_Sales` represents a single sales transaction.
- The transactional grain ensures accurate aggregation for measures such as sales, budget, profit, and variance across all dimensions.

## Notes
- The star schema supports fast aggregation and intuitive report filtering.
- `Dim_Date` should be configured as the active date table to support fiscal YTD and prior year time intelligence.
- Optional `Dim_Product` can be added when item-level sales detail is required.
