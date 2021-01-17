# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv
# Define location of CSV
csvpath = os.path.join('Resources', 'test.csv')

dict = {}
# Open csv
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(csv_header)
    
    total_votes = 0
# for loop that reads each row, checkin candidate row[indx]. if key exist increment value, 
# if not create key and give a value

    for row in csvreader:
        #set default key and value
        dict.setdefault((row[2]), 0)
        #increment by 1 every occurence
        dict[row[2]] += 1
        total_votes = total_votes + 1

winner = max([i for i in dict.values()])

print(dict)
print(total_votes)
print(winner)




