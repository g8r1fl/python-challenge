# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv
# Define location of CSV
csvpath = os.path.join('Resources', 'test.csv')

# Open csv
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(csv_header)
    
    voter_list = list(csvreader)
# print(len(voter_list))
    
def Extract(voter_list):
    return [item[2] for item in voter_list]

candidates = (Extract(voter_list))   
# print(candidates) 

# create empty dictionary
candidates_dict = {}

# update 'candidates_dict' with keys for each element (i) in 'candidates'
for i in range(len(candidates)):
    candidates_dict[candidates[i]] = candidates.count(candidates[i])

print(candidates_dict)    
    
