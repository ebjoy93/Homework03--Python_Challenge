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

#print(voteCount) #prints how many votes each canidate earned

##canidateCount = [voteCount]
votes = []
for p in voteCount.items():
    votes.append(int(p[1])) #places number of votes each canidate recieved into a list
#print(votes) #only prints number of votes each canidate received

#convVotes = list(map(int,votes))
#print(convVotes)

#canidateVotes = [int(i) for i in convVotes]
#intVotes = [int(a) for a in convInt]

votePercent = [p / len(convInt) for p in votes]
#print(votePercent)

print("Election Results")
print("--------------------------------------------------------")
print("Total Votes: " + str(len(convInt)))
print("---------------------------------------------------------")
print(voteCount[0] + votePercent[0])
