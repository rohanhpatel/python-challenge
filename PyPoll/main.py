import sys
import math
import csv
import os

# this function generates and returns a string that is used for output
def generateString(totVotes, votes, winner):
    s = "Election Results\n"
    s += "-------------------------\n"
    for key in votes:
        percentage = float(votes[key])/totVotes * 100
        s += f"{key}: {percentage:.3f}% ({votes[key]})\n"
    s += "-------------------------\n"
    s += f"Winner: {winner}\n"
    s += "-------------------------"
    return s

# create paths
csvPath = os.path.join(".", "Resources", "election_data.csv")
outputPath = os.path.join(".", "analysis", "output.txt")

with open(csvPath, encoding="UTF-8") as csvFile:
    csvReader = csv.reader(csvFile)
    csvHeader = list()
    # initialize dictionary
    votes = dict()
    firstLine = True
    # go through csv
    for line in csvReader:
        if not firstLine:
            # get candidate and add 1 to count for that specific candidate
            candidate = line[2]
            if candidate not in votes:
                votes[candidate] = 1
            else:
                votes[candidate] += 1
        else:
            firstLine = False
            csvHeader = line
    # get total votes using the votes for all candidates
    totVotes = 0
    for key in votes:
        totVotes += votes[key]
    maxVotes = -1
    winner = ""
    # get winner using the maximum of all the votes
    for key in votes:
        if votes[key] > maxVotes:
            winner = key
            maxVotes = votes[key]

    # now we print out results
    print(generateString(totVotes, votes, winner))

    # and we finally output results to "output.txt"
    with open(outputPath, "w") as outFile:
        outFile.write(generateString(totVotes, votes, winner))         