# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv
# Define location of CSV
csvpath = os.path.join('Resources', 'budget_data.csv')

# Open csv
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    print(csvreader)
    

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(csv_header)
    
    # define variables to hold new lists for solution
    Total_months = []
    profit_loss = []
    chg_pl = []

    # # Read each row of data after the header. Create new list for total months and profit/loss
    
    for row in csvreader:

        Total_months.append(row[0])
        profit_loss.append(int(row[1]))    
    
    # Print out analysis

    print("Financial Analysis")
    print("-------------------------------")
    print("Total Months:", len(Total_months))
    print("Total: ", "$ ", sum(profit_loss))

    # loop through the profit/loss list and subtract the next cell from the current cell
    for i in range(1,len(profit_loss)):
        chg_pl.append(profit_loss[i] - profit_loss[i-1])
        avg_chg = sum(chg_pl) / len(chg_pl)
    
    # set date variable for greatest increase/decrease in profit/loss    
    max_date = (Total_months[profit_loss.index(max(profit_loss))])
    min_date = (Total_months[profit_loss.index(min(profit_loss))])
    
    print("avg change: ", round(avg_chg,2))    
    
    print("Greatest Increase in profits: ", max_date, "$ ",max(profit_loss))
    print("Greatest Decrease in profits: ", min_date, "$ ",min(profit_loss))

import sys
# Save reference to original standard output
original_stdout = sys.stdout 

with open('Analysis/Analysis.txt', 'w') as f:
    # change std output to file w
    sys.stdout = f
    print("Financial Analysis")
    print("-------------------------------")
    print("Total Months:", len(Total_months))
    print("Total: ", "$ ", sum(profit_loss))
    print("avg change: ", round(avg_chg,2))    
    print("Greatest Increase in profits: ", max_date, "$ ",max(profit_loss))
    print("Greatest Decrease in profits: ", min_date, "$ ",min(profit_loss))
    sys.stdout = original_stdout
    
    



   
    
