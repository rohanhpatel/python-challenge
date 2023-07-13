import sys
import math
import csv
import os

#NEED TO COMMENT THIS FILE

csvPath = os.path.join(".", "Resources", "budget_data.csv")
outputPath = os.path.join(".", "analysis", "output.txt")

with open(csvPath, encoding="UTF-8") as csvFile:
    csvHeader = list()
    csvReader = csv.reader(csvFile, delimiter=",")
    firstLine = True
    totMonths = 0
    netPL = 0
    prevPL = None
    changes = list()
    biggestProfit = ["", -1]
    biggestLoss = ["", 1]
    for line in csvReader:
        if not firstLine:
            date = line[0]
            pl = int(line[1])
            totMonths += 1
            netPL += pl
            if prevPL != None:
                diff = pl - prevPL
                changes.append(diff)
                if diff > biggestProfit[1]:
                    biggestProfit = [date, diff]
                if diff < biggestLoss[1]:
                    biggestLoss = [date, diff]
            prevPL = pl
        else:
            firstLine = False
            csvHeader = line
    averageChanges = float(sum(changes))/len(changes)

    print("Finanical Analysis")
    print("----------------------------")
    print(f"Total Months: {totMonths}")
    print(f"Total: ${netPL}")
    print(f"Average Changes: ${averageChanges:.2f}")
    print(f"Greatest Increase in Profits: {biggestProfit[0]} (${biggestProfit[1]})")
    print(f"Greatest Decrease in Profits: {biggestLoss[0]} (${biggestLoss[1]})")
    
    with open(outputPath, "w") as outFile:
        outFile.write("Finanical Analysis\n")
        outFile.write("----------------------------\n")
        outFile.write(f"Total Months: {totMonths}\n")
        outFile.write(f"Total: ${netPL}\n")
        outFile.write(f"Average Changes: ${averageChanges:.2f}\n")
        outFile.write(f"Greatest Increase in Profits: {biggestProfit[0]} (${biggestProfit[1]})\n")
        outFile.write(f"Greatest Decrease in Profits: {biggestLoss[0]} (${biggestLoss[1]})")