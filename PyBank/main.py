# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    print(csvreader)
    

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(csv_header)
    
    # calculate total number of months in data
    # Total_months = len(list(csvreader))
    # print(f"Total months = {Total_months}")
    # print(Total_months)

    # # Read each row of data after the header
    total = 0  
    for row in csvreader:
        total += int(row[1])
    print(total)    
   
    
