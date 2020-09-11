import os
import csv

# Counter is used for counting total number of votes each candidate won
from collections import Counter

# set the path for the CSV file location 
pollCSV = os.path.join("..", "Resources", "election_data.csv")

# open the CSV file in "read" mode 
with open(pollCSV, "r") as csvFile:

    csvReader = csv.reader(csvFile, delimiter=",")

    # read the header row first
    csvHeader = next(csvFile)

    # variable to hold the total number of polls
    totalPoll = 0

    # list used to store the candidate names for every vote
    voteCandidateNames = []

    # read through each row of data after the header
    for row in csvReader:

        #increment total polls by 1 for every row read
        totalPoll += 1

        #store the names of candidate for each vote
        voteCandidateNames.append(row[2])

# Counter is used for counting total number of votes each candidate won
voteCounter = Counter(voteCandidateNames)

# save the candidate names as a list
candidateNames = voteCounter.keys()

# save the total votes for each candidate as a list
candidateVotes = voteCounter.values()

# save the vote percentage in a list
percentVotes = []
for votes in candidateVotes:
    percentVotes.append(round(int(votes)/totalPoll*100,3))

# determine the maximum vote
maxVote = max(candidateVotes)

# convert dict keys and dict values to list
candidateVotes = list(candidateVotes)
candidateNames = list(candidateNames)

# determine the winner's name
winnerName = candidateNames[candidateVotes.index(maxVote)]

# write the analysis results into a list
analysisData = []
analysisData.append("Election Results\n")
analysisData.append("-------------------------\n")
analysisData.append(f"Total Votes: {totalPoll}\n")
analysisData.append("-------------------------\n")

# write the percentage of votes and vote count for every candidate into list
for candidatesCount in range(0,len(candidateNames)):
    analysisData.append(f"{candidateNames[candidatesCount]}: {'{:.3f}'.format(percentVotes[candidatesCount])}% ({candidateVotes[candidatesCount]})\n")

# write the winner information into list
analysisData.append("-------------------------\n")
analysisData.append(f"Winner: {winnerName}\n")
analysisData.append("-------------------------\n")

# save the output file path
output_file = os.path.join("..","Analysis","election_analysis_report.txt")

# open the output file in "write" mode
with open(output_file, "w") as analysisFile:
    
    # write the results into the analysis text file
    analysisFile.writelines(analysisData)

    for line in analysisData:

        #remove the "\n" from end of every line
        line = line.split("\n")[0]

        #print the line to console
        print(line)
