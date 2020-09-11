import os
import csv

# set the path for the CSV file location 
budgetCSV = os.path.join("..", "Resources", "budget_data.csv")

# open the CSV file in "read" mode 
with open(budgetCSV, "r") as csvFile:

    csvReader = csv.reader(csvFile, delimiter=",")

    # read the header row first
    csvHeader = next(csvFile)

    # variable to hold the total number of months
    totalMonths = 0

    # list variable to hold the months
    months = []

    # list variable to hold the revenue(profit/losses)
    revenue = []

    # read through each row of data after the header
    for row in csvReader:

        # increment total months by 1 for every row read
        totalMonths += 1
        
        # store month data in a list
        months.append(row[0])

        # store revenue data in a list
        revenue.append(row[1])

print(totalMonths)