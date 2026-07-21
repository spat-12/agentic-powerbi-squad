# Sales Overview DAX Measures

## 1. Base Measures

```dax
Sales LC =
SUM(Fact_Sales[Sales_LC])
```

```dax
Budget LC =
SUM(Fact_Sales[Budget_LC])
```

```dax
Adjusted Profit LC =
SUM(Fact_Sales[Profit_LC])
```
```

## 2. Time Intelligence (YTD, PY, YOY)

```dax
Sales LC YTD =
CALCULATE(
    [Sales LC],
    TOTALYTD(
        Dim_Date[Date],
        "6/30"
    )
)
```

```dax
Budget LC YTD =
CALCULATE(
    [Budget LC],
    TOTALYTD(
        Dim_Date[Date],
        "6/30"
    )
)
```

```dax
Adjusted Profit LC YTD =
CALCULATE(
    [Adjusted Profit LC],
    TOTALYTD(
        Dim_Date[Date],
        "6/30"
    )
)
```

```dax
Sales LC PY =
CALCULATE(
    [Sales LC],
    SAMEPERIODLASTYEAR(Dim_Date[Date])
)
```

```dax
Budget LC PY =
CALCULATE(
    [Budget LC],
    SAMEPERIODLASTYEAR(Dim_Date[Date])
)
```

```dax
Sales LC YOY % =
VAR CurrentSales = [Sales LC]
VAR PriorSales = [Sales LC PY]
RETURN
DIVIDE(
    CurrentSales - PriorSales,
    ABS(PriorSales),
    BLANK()
)
```

```dax
Sales LC YTD PY =
CALCULATE(
    [Sales LC YTD],
    SAMEPERIODLASTYEAR(Dim_Date[Date])
)
```

```dax
Sales LC FY YOY % =
VAR CurrentYTD = [Sales LC YTD]
VAR PriorYTD = [Sales LC YTD PY]
RETURN
DIVIDE(
    CurrentYTD - PriorYTD,
    ABS(PriorYTD),
    BLANK()
)
```

## 3. Budget vs Actual Variance

```dax
Budget Variance LC =
[Sales LC] - [Budget LC]
```

```dax
Budget Variance % =
DIVIDE(
    [Sales LC] - [Budget LC],
    [Budget LC],
    0
)
```

```dax
Budget Achievement % =
DIVIDE(
    [Sales LC],
    [Budget LC],
    0
)
```

## 4. Profitability Measures

```dax
Adjusted Profit % =
DIVIDE(
    [Adjusted Profit LC],
    [Sales LC],
    0
)
```

```dax
Adjusted Profit % YTD =
DIVIDE(
    [Adjusted Profit LC YTD],
    [Sales LC YTD],
    0
)
```

```dax
Average Monthly Sales =
VAR MonthsSelected =
    DISTINCTCOUNT(Dim_Date[MonthYear])
RETURN
DIVIDE(
    [Sales LC],
    MonthsSelected,
    0
)
```

## 5. KPI Indicators

```dax
Budget Status =
VAR VariancePct = [Budget Variance %]
RETURN
SWITCH(
    TRUE(),
    VariancePct >= 0.05, "Green",
    VariancePct >= -0.05, "Yellow",
    "Red"
)
```

```dax
Profit Status =
VAR ProfitPct = [Adjusted Profit %]
RETURN
SWITCH(
    TRUE(),
    ProfitPct >= 0.15, "Green",
    ProfitPct >= 0.08, "Yellow",
    "Red"
)
```

```dax
Sales vs Budget Index =
DIVIDE(
    [Sales LC],
    [Budget LC],
    0
)
```

```dax
Sales Growth vs PY % =
VAR CurrentSales = [Sales LC]
VAR PriorSales = [Sales LC PY]
RETURN
DIVIDE(
    CurrentSales - PriorSales,
    ABS(PriorSales),
    BLANK()
)
```
