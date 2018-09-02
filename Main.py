# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('.', 'budget_data.csv')

# # Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))


# Method 2: Improved Reading using CSV module

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # print(csvreader)

    # # Read the header row first (skip this step if there is now header)
    # csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    # for row in csvreader:
        # print(row)

    # The total number of months included in the dataset
    counter = 0
    NetProfitorLoss = 0
    PriorMonth = 0
    StoreTotalChanges = 0
    AverageChangeinProfitandLosses = 0
    GreatestIncrease = ["", 0]
    for row in csvreader:
        if counter != 0:
            #The total net amount of "Profit/Losses" over the entire period
            NetProfitorLoss = NetProfitorLoss + int(row[1])
            current = (row[1])
            if counter > 1:
                StoreTotalChanges = StoreTotalChanges + int(current) - int(PriorMonth)
            #print (str(StoreTotalChanges))
            PriorMonth = current
            #Loop through StoreTotalChange and compare number to find the greatest increase and greatest decrease
            if (StoreTotalChanges > GreatestIncrease[1]):
                    GreatestIncrease[1] = StoreTotalChanges



        # Print the values

        counter = counter + 1  
    print("Financial Analysis" )  
    print("-----------------------------------------")
    print ("Total Months: " + str(counter - 1))
    print ("Total: " + "$" + str(NetProfitorLoss))
    AverageChangeinProfitandLosses = round((StoreTotalChanges)/(counter - 2), 2)
    
    # The average change in "Profit/Losses" between months over the entire period 
    print ("Average Change: " + "$" + str(AverageChangeinProfitandLosses))

    #Print the greatest increase in profits (date and amount) over the entire period
    print(GreatestIncrease[1])
