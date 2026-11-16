# Reflection 1:
# This is like using Excel to open a sales file, calculate totals, and filter rows.
# Python makes it easier to repeat the same steps on many files without doing
# everything by hand, while Excel makes quick edits and charts easier to see.
#
# Reflection 2:
# A brewery could log its daily sales total after closing each night.
# Append mode keeps the earlier entries and adds the newest one at the bottom,
# so the manager can review past days without losing any records.

import csv
from datetime import datetime

# Exercises 1 and 2: Open the file and print all rows, including the header.
print("Raw rows:")
with open("data/sales.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
# The prices and quantities are still strings here.

# Exercise 3: Save and skip the header.
print("\nHeader and data rows:")
with open("data/sales.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    header = next(reader)
    print("Header:", header)
    for row in reader:
        print(row)

# Exercise 4: Convert the numbers and calculate revenue.
print("\nRevenue by order:")
total_revenue = 0
original_count = 0
with open("data/sales.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])
        total = round(price * quantity, 2)
        total_revenue += total
        original_count += 1
        print(f"{product}: {quantity} units × ${price:.2f} = ${total:.2f}")
print(f"Total revenue: ${total_revenue:.2f}")
