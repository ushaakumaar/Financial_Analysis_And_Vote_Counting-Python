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

# variable to store the net total amount of "Profit/Losses" over the entire period
netAmount = 0

# calculate average of the changes in "Profit/Losses" over the entire period
avgChange = round((int(revenue[totalMonths-1]) - int(revenue[0]))/(totalMonths-1),2)

# loop through the list
for index in range(0,totalMonths):

    # calculate the net total amount of "Profit/Losses" over the entire period
    netAmount += int(revenue[index])

print(totalMonths)
print(netAmount)
print(avgChange)