# import operating system and csv
import os
import csv

# write csv file path
csvpath = os.path.join('Resources', 'election_data.csv')

# create list/dict for candidate info/counting votes
candidate_list = []
candidate_dict = {}
totalvotes = []
candidate_percent = []

# create statement to open csvfile handle
with open(csvpath) as csvfile:

    # open csv as reader
    csvreader = csv.reader(csvfile, delimiter= ",")

    # identify csv header
    csv_header = next(csvreader)

    # name variable to count voters 
    row_count = 0

    # loop over csv content
    for row in csvreader:

        # in an if statement, write list to count total votes
        if row_count > 0:
            totalvotes.append(str(row[2]) == str(previous_row[2]))
        else:
            previous_row = row

        # rows moving incrementally by one
        row_count += 1

        # variable for candidate name
        candidate_name = row[2]

        # write if statement to count candidates
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            candidate_dict[candidate_name] = 0

        # count votes per candidate
        candidate_dict[candidate_name] += 1


# define variables for winner    
top_candidate = 0
winner_name = ''

# print findings to terminal
title = print ('Election Results')
print('--------------------------------------')
print(f'Total Votes: {row_count:d}')
print('--------------------------------------')
for key in candidate_dict:
    candidate_percent = (candidate_dict[key]/row_count)*100
    print(f'{key}: {candidate_dict[key]}, {candidate_percent:0.3f}%')
    if candidate_dict[key] > top_candidate:
        top_candidate = candidate_dict[key]
        winner_name = key
print('--------------------------------------')
print(f'Winner: {winner_name}')


# create final analysis path
analysispath = os.path.join('analysis', 'pypoll_analysis.txt')

# print findings to new text file
with open(analysispath, 'w') as analysis_file:
    analysis_file.write('Election Results\n')
    analysis_file.write('--------------------------------------\n')
    analysis_file.write('Total Votes: %d\n' %(row_count))
    analysis_file.write('--------------------------------------\n')
    for key in candidate_dict:
        candidate_percent = (candidate_dict[key]/row_count)*100
        analysis_file.write('%s: %d %0.3f%%\n' %(key , candidate_dict[key] , candidate_percent))
        if candidate_dict[key] > top_candidate:
            top_candidate = candidate_dict[key]
            winner_name = key
    analysis_file.write('--------------------------------------\n')
    analysis_file.write('Winner: %s\n' %(winner_name))

    analysis_file.close()