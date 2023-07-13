import sys
import math
import csv
import os

# COMMENT THIS FILE

csvPath = os.path.join(".", "Resources", "election_data.csv")
outputPath = os.path.join(".", "analysis", "output.txt")

with open(csvPath, encoding="UTF-8") as csvFile:
    csvReader = csv.reader(csvFile)
    csvHeader = list()
    votes = dict()
    firstLine = True
    for line in csvReader:
        if not firstLine:
            candidate = line[2]
            if candidate not in votes:
                votes[candidate] = 1
            else:
                votes[candidate] += 1
        else:
            firstLine = False
            csvHeader = line

    totVotes = 0
    for key in votes:
        totVotes += votes[key]
    maxVotes = -1
    winner = ""
    for key in votes:
        if votes[key] > maxVotes:
            winner = key
            maxVotes = votes[key]
    print("Election Results")
    print("-------------------------")
    for key in votes:
        percentage = float(votes[key])/totVotes * 100
        print(f"{key}: {percentage:.3f}% ({votes[key]})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

    with open(outputPath, "w") as outFile:
        outFile.write("Election Results\n")
        outFile.write("-------------------------\n")
        for key in votes:
            percentage = float(votes[key])/totVotes * 100
            outFile.write(f"{key}: {percentage:.3f}% ({votes[key]})\n")
        outFile.write("-------------------------\n")
        outFile.write(f"Winner: {winner}\n")
        outFile.write("-------------------------")            
    
    

