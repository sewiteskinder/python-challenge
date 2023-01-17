# import operating system/csv file
import os
import csv

# create csv file path
csvpath = os.path.join('Resources', 'budget_data.csv')

# define variables for arrays used in profit/loss changes and inc/dec
change_profitloss_list = []
greatest_profit_list = []

# create statement to open csvfile handle
with open(csvpath) as csvfile:

    # open csv as reader
    csvreader = csv.reader(csvfile, delimiter=",")

    # identify csv header
    csv_header = next(csvreader)

    # more variables for row count/total profits
    row_count = 0

    total_profits = 0

    # define greatest inc/dec variables

    inc_profit = 0
    dec_profit = 0


    # loop over csv content
    for row in csvreader:

        # in if statement, write array to store change in profits
        if row_count > 0:
            change_profitloss_list.append(int(row[1]) - int(previous_row[1]))
            previous_row = row
        else:
            previous_row = row
        
        # rows moving incrementally by 1
        row_count += 1

        # define variables to hold total profits of whole csv
        profit_loss = int(row[1])
        total_profits += profit_loss

    # set average change variable
    change_average_total = 0

    # loop over change in profits to find total changes during entire period
    for change_profitloss in change_profitloss_list:
        change_average_total += change_profitloss 
    
    # find average change of profits over period
    change_average = int(change_average_total) / len(change_profitloss_list)

    # loop to find greatest profit inc/dec
    for min_max in change_profitloss_list:

        if int(min_max) > inc_profit:
            inc_profit = int(min_max)

        if int(min_max) < dec_profit:
            dec_profit = int(min_max)
       
    # print final findings
    title = print("Financial Analysis")
    print("--------------------------------------") 
    print (f'Total Months: {row_count:d}')
    print (f'Net Total: ${total_profits:d}')
    print (f'Average Change: ${change_average:0.2f}')
    print (f'Greatest Increase in Profits: ${inc_profit:d}')
    print (f'Greated Decrease in Profits: ${dec_profit:d}')

    # create final analysis path
    analysispath = os.path.join('analysis', 'pybank_analysis.txt')
    
    with open(analysispath, 'w') as analysis_file:
        analysis_file.write("Financial Analysis\n")
        analysis_file.write("--------------------------------------\n")
        analysis_file.write("Total Months: %d\n" %(row_count))
        analysis_file.write("Net Total: $%d\n" %(total_profits))
        analysis_file.write("Average Change: $%0.2f\n" %(change_average))
        analysis_file.write("Greatest Increase in Profits: $%d\n" %(inc_profit))
        analysis_file.write("Greated Decrease in Profits: $%d\n" %(dec_profit))

    analysis_file.close()
