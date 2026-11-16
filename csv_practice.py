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

# Exercise 5: Write only orders over $100.
written_count = 0
with open("data/sales.csv", "r", newline="", encoding="utf-8") as source:
    reader = csv.reader(source)
    next(reader)
    with open("data/cleaned.csv", "w", newline="", encoding="utf-8") as output:
        writer = csv.writer(output)
        writer.writerow(["Product", "Price", "Qty", "Total"])
        for row in reader:
            product = row[0]
            price = float(row[1])
            quantity = int(row[2])
            total = round(price * quantity, 2)
            if total > 100:
                writer.writerow([product, f"{price:.2f}", quantity, f"{total:.2f}"])
                written_count += 1
print(f"\nWrote {written_count} of {original_count} original rows to data/cleaned.csv.")

# Exercise 6: Read the columns by name.
# I would use reader for a small file when I already know the column order.
# I would use DictReader when named columns make the code easier to follow.
print("\nDictReader totals:")
dict_total = 0
with open("data/sales.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])
        total = round(price * quantity, 2)
        dict_total += total
        print(f"{product}: {quantity} units × ${price:.2f} = ${total:.2f}")
print(f"DictReader total revenue: ${dict_total:.2f}")
print("Totals match:", round(dict_total, 2) == round(total_revenue, 2))

# Exercise 7: Add up repeated products and sort by name.
summary = {}
with open("data/sales.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        product = row["product"]
        total = round(float(row["price"]) * int(row["quantity"]), 2)
        summary[product] = summary.get(product, 0) + total

print("\nSales summary by product:")
for product in sorted(summary):
    print(f"{product}: ${summary[product]:.2f}")

# Exercise 8: Keep the old log entries and add one for this run.
timestamp = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %z")
with open("data/run_log.txt", "a", encoding="utf-8") as log:
    log.write(f"{timestamp} - Total revenue: ${total_revenue:.2f}\n")
print("\nAdded this run to data/run_log.txt.")
