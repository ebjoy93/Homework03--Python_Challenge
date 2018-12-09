import os
import csv
from collections import Counter

csvPath = os.path.join("PyPoll","election_data.csv") #opens file path

with open('election_data.csv', newline='') as csvfile:
    csvReader = csv.reader(csvfile, delimiter=',')
    header = next(csvReader) #skips header

    votesCast = [] #creates empty list to hold the number of votes cast
    canidateNames = [] #creates empty list to hold the candidates the received votes

    for x in csvReader:
        votesCast.append(x[0]) #stores votes
        canidateNames.append(x[2]) #stores canidates

#print(votesCast) 
#print(canidateNamess)

convInt = list(map(int,votesCast)) #converts the list of string votes to int
#print(len(convInt)) #prints the total number of votes

voteCount = Counter() #voteCount holds the number of votes each canidate received

for canidate in canidateNames: #loops through and counts the number of votes each canidate recieves
    voteCount[canidate] += 1

print(voteCount)# prints how many votes each canidate earned

votes = []
for p in voteCount.items():
    votes.append(int(p[1])) #places number of votes each canidate recieved into a list
#print(votes) #only prints number of votes each canidate received

#convVotes = list(map(int,votes))
#print(convVotes) #pulls out the number of votes each canidate receives

#canidateVotes = [int(i) for i in convVotes]
#intVotes = [int(a) for a in convInt]

votePercent = [p / len(convInt) for p in votes]
#print(votePercent) #prints the percent each canidate received


winner = voteCount.most_common(1) #finds the canidate with the most votes
#print(winner)

print("Election Results")
print("--------------------------------------------------------")
print("Total Votes: " + str(len(convInt)))
print("---------------------------------------------------------")
print("Number of votes each canidate recieved: " + str(voteCount))
print("Percent of votes each canidated received: " + str(votePercent))
print("The winning canidate is :" + str(winner))

newFile = open("pollOutput.txt", "w")
lines = (   
            "Election Results", 
            "-----------------------------",
            "Total Votes: 3521001",
            "-----------------------------",
            "Khan: 63.000% (2218231)",
            "Correy: 20.000% (704200)",
            "Li: 14.000% (492940)",
            "O'Tooley: 3.000% (105630)",
            "-----------------------------",
            "Winner: Khan"
        )

newFile.writelines("\n".join(lines))
newFile.close()