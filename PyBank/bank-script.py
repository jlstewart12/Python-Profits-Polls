import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")
analysis = os.path.join("analysis", "budget_analysis.txt")

changes = []
months = 0
net_changes = []
max_increase = ['', 0]
max_decrease = ['', 9999999999999]
net_sum = 0

with open(budget_csv) as financial_data:
    reader = csv.reader(financial_data)

    header = next(reader)

    first_row = next(reader)
    months = months + 1
    net_sum = net_sum + int(first_row[1])
    prev_net = int(first_row[1])

    for row in reader:
        months = months + 1
        net_sum = net_sum + int(row[1])

        net_changes = int(row[1]) - prev_net
        prev_net = int(first_row[1])
        changes = changes + [net_changes]
        months = months + [row[0]]
    
        if net_changes > max_increase[1]:
            max_increase[0] = row[0]
            max_increase[0] = net_changes

        if net_changes < max_decrease[1]:
            max_increase[0] = row[0]
            max_increase[0] = net_changes

net_monthly_avg = sum(changes)/len(changes)

output = (
    f"\nFinancial Analysis\n"
    f"---------------------------\n"
    f"Total Months: {months}\n"
    f"Total: ${net_sum}\n"
    f"Average Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {max_increase[0]} (${max_increase[1]})\n"
    f"Greatest Decdrease in Profits: {max_decrease[0]} (${max_decrease[1]})\n")

print(output)

with open(analysis, "w") as txt_file:
    txt_file.write(output)