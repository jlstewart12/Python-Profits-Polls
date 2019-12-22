import os
import csv

budget_csv = os.path.join("budget_data.csv")

with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    budget_data = next(csvreader)
print(f"CSV Header: {csv_header}")

changes = []
months = 0
net_rev = 0
max_net = 0
min_net = 0
max_mo = ""
min_mo = ""
first_mo = ""
first_net= 0

# Read each row of data after the header
for row in budget_csv:
    if first_mo !="":
        change = int(row[1]) - first_net
        changes.append(change)
        if change > max_net:
            max_net = change
            max_mo = row[0]
        if change < min_net:
            min_net = change
            min_mo = row[0]
    first_net = int(row[1])
    first_mo = row[0]
    months += 1
    net_rev += int(row[1])
    avg_change = avg(changes)

print(f"Total Months: {months}")
print(f"Total Revenue: {net_rev}")
