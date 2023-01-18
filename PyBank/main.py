# import operating system/csv file
import os
import csv

# create csv file path
csvpath = os.path.join('Resources', 'budget_data.csv')

# name lists used in profit/loss changes and inc/dec
greatest_dec_list = ["",0]
greatest_inc_list = ["", 0]
change_profitloss_list = []

# create statement to open csvfile handle
with open(csvpath) as csvfile:

    # open csv as reader
    csvreader = csv.reader(csvfile, delimiter=",")

    # identify csv header
    csv_header = next(csvreader)

    # name variables for row count/total profits
    row_count = 0
    total_profits = 0

    # define greatest inc/dec variables
    inc_date = ''
    dec_date = ''

    # loop over csv content
    for row in csvreader:

        # in if statement, write array to store change in profits
        if row_count > 0:
            change_profitloss_list.append(int(row[1]) - int(previous_row[1]))
            change = int(row[1]) - int(previous_row[1])

            if change > greatest_inc_list[1]:
                greatest_inc_list[1] = change
                greatest_inc_list[0] = row[0]

            if change < greatest_dec_list[1]:
                greatest_dec_list[1] = change
                greatest_dec_list[0] = row[0]

            previous_row = row
        else:
            previous_row = row

        # rows moving incrementally by 1
        row_count += 1

        # define variables to hold total profits of whole csv
        profit_loss = int(row[1])
        total_profits += profit_loss

    # print findings to terminal
    print(f'Financial Analysis')
    print('--------------------------------------')
    print(f'Total Months: {row_count:d}')
    print(f'Net Total: ${total_profits:d}')
    print(f'Average Change: ${sum(change_profitloss_list)/len(change_profitloss_list):0.2f}')
    print(f'Greatest Increase in Profits: {greatest_inc_list[0]} ${greatest_inc_list[1]}')
    print(f'Greatest Decrease in Profits: {greatest_dec_list[0]} ${greatest_dec_list[1]}')



    # create final analysis path
    analysispath = os.path.join('analysis', 'pybank_analysis.txt')

    # print findings to new text file
    with open(analysispath, 'w') as analysis_file:
        analysis_file.write('Financial Analysis\n')
        analysis_file.write('--------------------------------------\n')
        analysis_file.write('Total Months: %d\n' %(row_count))
        analysis_file.write('Net Total: $%d\n' %(total_profits))
        analysis_file.write('Average Change: $%0.2f\n' %(sum(change_profitloss_list)/len(change_profitloss_list)))
        analysis_file.write('Greatest Increase in Profits: %s $%d\n' %(greatest_inc_list[0] , greatest_inc_list[1]))
        analysis_file.write('Greatest Decrease in Profits: %s $%d\n' %(greatest_dec_list[0] , greatest_dec_list[1]))

    analysis_file.close()

