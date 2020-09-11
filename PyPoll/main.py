import os
import csv

# Set the path for the CSV file location 
pollCSV = os.path.join("..", "Resources", "election_data.csv")

# Open the CSV file in "read" mode 
with open(pollCSV, "r") as csvFile:

    csvReader = csv.reader(csvFile, delimiter=",")

    # Read the header row first
    csvHeader = next(csvFile)

    # variable to hold the total number of polls
    totalPoll = 0

    # Read through each row of data after the header
    for row in csvReader:

        #increment total polls by 1 for every row read
        totalPoll += 1

# write the analysis results into a list
analysisData = []
analysisData.append("Election Results\n")
analysisData.append("-------------------------\n")
analysisData.append(f"Total Votes: {totalPoll}\n")
analysisData.append("-------------------------\n")

# save the output file path
output_file = os.path.join("..","Analysis","election_analysis_report.txt")

# open the output file in "write" mode
with open(output_file, "w") as analysisFile:
    
    # write the results into the analysis text file
    analysisFile.writelines(analysisData)

    for line in analysisData:

        #remove the "\n" from end of every line
        line = line[0:len(line)-2]

        #print the line to console
        print(line)


