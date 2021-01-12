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
    # print(csv_header)
    
    # calculate total number of months in data
    Total_months = []
    profit_loss = []
    chg_pl = []

    # # Read each row of data after the header. Create new list for total months and profit/loss
    
    for row in csvreader:

        Total_months.append(row[0])
        profit_loss.append(int(row[1]))    
    
    # Print out analysis
    print(len(Total_months))
    print(sum(profit_loss))
    print("Financial Analysis")
    print("-------------------------------")
    print("Total Months:", len(Total_months))
    print("Total: ", sum(profit_loss))

    # loop through the profit/loss list and subtract the next cell from the current cell
    for i in range(1,len(profit_loss)):
        chg_pl.append(profit_loss[i] - profit_loss[i-1])
        avg_chg = sum(chg_pl) / len(chg_pl)
    print("avg change: ", avg_chg)    

    print("Greatest Increase in profits: ",max(profit_loss))
    print("Greatest Decrease in profits: ",min(profit_loss))


   
    
