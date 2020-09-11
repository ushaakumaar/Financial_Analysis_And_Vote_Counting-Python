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

# variable to save previous revenue
prevRevenue = 0

# variable to store the greatest increase in profits amount over the entire period
highestProfit = 0

# variable to store the month with the greatest increase in profits amount over the entire period
highestProfitMonth = ""

# variable to store the greatest decrease in losses amount over the entire period
highestLoss = 0

# variable to store the month with the greatest decrease in losses amount over the entire period
highestLossMonth = ""

# variable to store change in "profit/losses"
change = 0

# loop through the list
for index in range(0,totalMonths):

    # calculate the net total amount of "Profit/Losses" over the entire period
    netAmount += int(revenue[index])

    if index == 0:
        # initialize prevRevenue to the first profit/loss
        prevRevenue = int(revenue[index])
    else:
        # compute the change in profit/losses
        change = int(revenue[index]) - prevRevenue

        # find the greatest increase in profits amount/date over the entire period
        if change > highestProfit:
            highestProfit = change
            highestProfitMonth = months[index]
        # find the greatest decrease in losses amount/date over the entire period
        elif change < highestLoss:
            highestLoss = change
            highestLossMonth = months[index]

        # assign the current value to previous for the next iteration
        prevRevenue = int(revenue[index])

# write the analysis results into a list
analysisData = []
analysisData.append("Financial Analysis\n")
analysisData.append("-------------------------\n")
analysisData.append(f"Total Months: {totalMonths}\n")
analysisData.append(f"Total: ${netAmount}\n")
analysisData.append(f"Average  Change: ${avgChange}\n")
analysisData.append(f"Greatest Increase in Profits: {highestProfitMonth} (${highestProfit})\n")
analysisData.append(f"Greatest Decrease in Profits: {highestLossMonth} (${highestLoss})\n")
analysisData.append("-------------------------\n")

# save the output file path
output_file = os.path.join("..","Analysis","bank_analysis_report.txt")

# open the output file in "write" mode
with open(output_file, "w") as analysisFile:
    
    # write the results into the analysis text file
    analysisFile.writelines(analysisData)

    for line in analysisData:

        #remove the "\n" from end of every line
        line = line.split("\n")[0]