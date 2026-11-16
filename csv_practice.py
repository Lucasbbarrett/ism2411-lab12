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
