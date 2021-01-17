# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv
# Define location of CSV
csvpath = os.path.join('Resources', 'election_data.csv')

# create blank dict
# Open csv
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(csv_header)
    

    # for loop that reads each row, checkin candidate row[indx]. if key exist increment value, 
    # if not create key and give a value
    candidates = []
    dict ={}
    keys_list = list(dict)
    # key = keys_list[]
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

    Khan_votes = dict.get(list(dict)[0])             
    print("Election Results")
    print("------------------------")
    print("Total Votes: " , counter)
    print("------------------------")
    print(list(dict)[0])
    print(list(dict)[1])
    print(counter)
    print(dict)
    print(Khan_votes)
    print(counter)
    # print csvreader to list of lists
    # voter_list = list(csvreader)

# Extract just the candidates from list
# def Extract(voter_list):
#     return [item[2] for item in voter_list]
# # assign new list to candidates
# candidates = (Extract(voter_list))       

# # create empty dictionary
# candidates_dict = {}

# # update 'candidates_dict' with keys for each element (i) in 'candidates'
# for i in range(len(candidates)):
#     candidates_dict[candidates[i]] = candidates.count(candidates[i])

# print(candidates_dict) 








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
