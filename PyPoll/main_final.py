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

    # winner = max([i for i in dict.values()])
    winner = max(dict,key=dict.get)
    Khan_votes = dict.get(list(dict)[0])
    khan_perc = int((Khan_votes / total_votes) * 100)
    Correy_votes = dict.get(list(dict)[1])
    correy_perc = int((Correy_votes / total_votes) * 100)
    Li_votes = dict.get(list(dict)[2])
    li_perc = int((Li_votes / total_votes) * 100)
    OTooley_votes = dict.get(list(dict)[3]) 
    otool_perc = int((OTooley_votes / total_votes) * 100)         
    print("Election Results")
    print("------------------------")
    print("Total Votes: " , total_votes)
    print("------------------------")
    print(list(dict)[0],":" , khan_perc,"%  " , "" , Khan_votes)
    print(list(dict)[1],":" , correy_perc,"%  " , ""  , Correy_votes)
    print(list(dict)[2],":" , li_perc,"% " , "" , Li_votes)
    print(list(dict)[3],":" , otool_perc,"% " , "" , OTooley_votes)
    print("------------------------")
    print("Winner: " , winner )
    print("------------------------")
    print(dict)


import sys
# Save reference to original standard output
original_stdout = sys.stdout 

with open('Analysis.txt', 'w') as f:
    # change std output to file w
    sys.stdout = f
    print("Election Results")
    print("------------------------")
    print("Total Votes: " , total_votes)
    print("------------------------")
    print(list(dict)[0],":" , khan_perc,"%  " , "" , Khan_votes)
    print(list(dict)[1],":" , correy_perc,"%  " , ""  , Correy_votes)
    print(list(dict)[2],":" , li_perc,"% " , "" , Li_votes)
    print(list(dict)[3],":" , otool_perc,"% " , "" , OTooley_votes)
    print("------------------------")
    print("Winner: " , winner )
    print("------------------------")
    sys.stdout = original_stdout


