# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('.', 'budget_data.csv')
newfile = os.path.join('.', 'pyBankResults.txt')

# # Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))

FilePrint=[]
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
    GreatestIncrease =0 
    GreatestDate = 0
    LowestIncrease = 9999999999
    LowestDate = 0
    for row in csvreader:
        if counter != 0:
            #The total net amount of "Profit/Losses" over the entire period
            NetProfitorLoss = NetProfitorLoss + int(row[1])
            current = (row[1])
            if counter > 1:
                StoreTotalChanges = StoreTotalChanges + int(current) - int(PriorMonth)
            currentchange = int(current) - int(PriorMonth)
            #print (str(StoreTotalChanges))
            PriorMonth = current
            #Loop through StoreTotalChange and compare number to find the greatest increase and greatest decrease
            if (currentchange > GreatestIncrease):
                    GreatestIncrease = currentchange
                    GreatestDate = row[0]
            if (currentchange < LowestIncrease):
                    LowestIncrease = currentchange
                    LowestDate = row[0]


        # Print the values

        counter = counter + 1  
    FilePrint.append("Financial Analysis" + "\n" )  
    FilePrint.append("-----------------------------------------"+ "\n")
    FilePrint.append("Total Months: " + str(counter - 1)+ "\n")
    FilePrint.append("Total: " + "$" + str(NetProfitorLoss)+ "\n")
    AverageChangeinProfitandLosses = round((StoreTotalChanges)/(counter - 2), 2)
    
    # The average change in "Profit/Losses" between months over the entire period 
    FilePrint.append("Average Change: " + "$" + str(AverageChangeinProfitandLosses)+ "\n")

    #Print the greatest increase in profits (date and amount) over the entire period
    FilePrint.append("Greatest Increase in Profits: "+GreatestDate+" ("+str(GreatestIncrease)+")"+ "\n")
    FilePrint.append("Greatest Decrease in Profits: "+LowestDate+" ("+str(LowestIncrease)+")"+ "\n")

with open(newfile, "w") as txtfile:
    txtfile.writelines(FilePrint)