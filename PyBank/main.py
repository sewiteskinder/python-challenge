import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

title = print("Financial Analysis")
print("--------------------------------------")

Date = []
Profit_Losses = []

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    row_count = 0

    total_profits = 0

    for row in csvreader:

        row_count += 1

        profit_loss = int(row[1])
        total_profits += profit_loss
       
    print (f'Total Months: {row_count:d}')
    print (f'Net Total: {total_profits:d}')
