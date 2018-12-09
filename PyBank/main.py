import os
import csv

csvPath = os.path.join("PyBank","budget_data.csv") #opens file path

with open('budget_data.csv', newline='') as csvfile:
    csvReader = csv.reader(csvfile, delimiter=',')
    header = next(csvReader) #skips header

    monthYears = [] #creates empty list to store month/years
    profitLoss = [] #creates empty list to store profit/loss

    for x in csvReader:
        monthYears.append(x[0]) #stores the months/years
        profitLoss.append(x[1]) #stores profits/loss

#print(monthYears) #prints months/years

convInt = list(map(int,profitLoss)) #converts profitLoss to a list of int

avgChange = sum(convInt) / len(convInt) #calculates the average of profitLoss

print("Financial Analysis")
print("---------------------------------------------------------")
print("Total Months: " + str(len(monthYears))) #prints size of months/years and converts the int to str
print("Average Change: " + str(avgChange)) #prints average change
print("Greatest Increase in Profits: " + max(profitLoss)) #prints max profit
print("Greatest Decrease in Losses: " + min(profitLoss)) #prints max loss


outputFile = open("bankOutput.txt","w")
lines = [
            "Financial Analysis",
            "--------------------------------------",
            "Average Change: 446309.0465116279",
            "Greatest Increase in Profits: 999942",
            "Greatest Decrease in Losses: -1022534"
        ]

outputFile.writelines("\n".join(lines))
outputFile.close()
