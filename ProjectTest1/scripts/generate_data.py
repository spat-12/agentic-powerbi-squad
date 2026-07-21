import csv
import os
import random
from datetime import date, timedelta

# Output directory (project-local)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
OUT_DIR = os.path.join(BASE_DIR, 'data')
os.makedirs(OUT_DIR, exist_ok=True)

# --------------------
# DIM TABLES
# --------------------
areas = ['NT','SA','NSW','VIC','QLD','WA','ACT']
staff = ['SP001','SP002','SP003','SP004','SP005']
customers = ['CU001','CU002','CU003','CU004','CU005']
products = ['PR001','PR002','PR003','PR004','PR005']

# --------------------
# DIM_DATE
# --------------------
start = date(2025, 7, 1)
end = date(2026, 6, 30)

dates = []
current = start
while current <= end:
    dates.append({
        'Date': current.isoformat(),
        'Year': current.year,
        'Month': current.month,
        'MonthYear': current.strftime('%b %Y')
    })
    current += timedelta(days=1)

with open(os.path.join(OUT_DIR, 'Dim_Date.csv'), 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=dates[0].keys())
    writer.writeheader()
    writer.writerows(dates)

# --------------------
# SIMPLE DIM TABLES
# --------------------
with open(os.path.join(OUT_DIR, 'Dim_Geography.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['AreaID'])
    for area in areas:
        writer.writerow([area])

with open(os.path.join(OUT_DIR, 'Dim_Staff.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['SalespersonID'])
    for s in staff:
        writer.writerow([s])

with open(os.path.join(OUT_DIR, 'Dim_Customer.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['CustomerID'])
    for c in customers:
        writer.writerow([c])

with open(os.path.join(OUT_DIR, 'Dim_Product.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['ProductID'])
    for p in products:
        writer.writerow([p])

# --------------------
# FACT TABLE
# --------------------
rows = []

for i in range(100):
    sales = round(random.uniform(5000, 50000), 2)
    budget = round(sales * random.uniform(0.8, 1.2), 2)
    profit = round(sales * random.uniform(0.1, 0.2), 2)

    rows.append({
        'TransactionID': f'TX{i}',
        'DateKey': random.choice(dates)['Date'],
        'AreaID': random.choice(areas),
        'SalespersonID': random.choice(staff),
        'CustomerID': random.choice(customers),
        'ProductID': random.choice(products),
        'Sales_LC': sales,
        'Budget_LC': budget,
        'Profit_LC': profit
    })

with open(os.path.join(OUT_DIR, 'Fact_Sales.csv'), 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

print(f"✅ CSV files generated in {OUT_DIR}")
