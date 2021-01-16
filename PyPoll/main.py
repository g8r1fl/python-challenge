# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv
# Define location of CSV
csvpath = os.path.join('Resources', 'election_data.csv')

# Open csv
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    print(csvreader)
    

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(csv_header)
    
    voter_list = list(csvreader)

def Extract(voter_list):
    return [item[2] for item in voter_list]

candidate_list = Extract(voter_list)       
print(len(candidate_list))
    # define variables to hold new lists for solution
    # vote_count = []
    # candidates = []

    # Read each row of data after the header  
    # for row in csvreader:
    #      if row[0] == 'Voter ID':
    #          pass
    #      else:
    #          if row[2] not in candidates:
    #              candidates.append(row[2])
    #          else:
    #              pass


    # print(candidates)
