# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv
# Define location of CSV
csvpath = os.path.join('Resources', 'test.csv')

# create blank dict
# election_dict = {}

# Open csv
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(csv_header)

    candidates = []
    dict ={}
    counter = 0
# Read each row of data after the header  
    for row in csvreader:
         if row[0] == 'Voter ID':
             pass
         else:
             if row[2] not in candidates:
                 candidates.append(row[2])
                 dict[row[2]] = ""
             else:
                 counter = counter + 1
                 pass


    print(candidates)
    print(dict)
    print(counter)
   
    
# for loop that reads each row, checkin candidate row[indx]. if key exist increment value, 
# if not create key and give a value


