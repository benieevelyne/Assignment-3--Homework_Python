# Import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('.', 'election_data.csv')
newfile = os.path.join('.', 'PyPollResults.txt')

# Method to improve reading using CSV module

FilePrint = []

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # print(csvreader)
    
    # Set list to help the following:
    # # The total number of votes cast
    Voter_IDs = []
    TotalNumberofVotes = 0
    # # Get a complete list of candidates who received votes
    candidates = []
    CandidateNameList = []
    name = 0
    PercentageCalculated = 0
    numberofVotersPerCandidates = []
    PercentageofVotersPerCandidates = []
    TupleList = []
    FinalResults = []
    Winner = 0
    # # The percentage of votes each candidate won
    
    # # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    
    #Read each row of data after the header
    for row in csvreader:
        Voter_ID = row[0]
        Voter_IDs.append(Voter_ID)
        candidate = row[2]
        candidates.append(candidate) 
    
    TotalNumberofVotes = len(Voter_IDs)
    CandidateNameList = list(set(candidates))
    
    for name in CandidateNameList:
        CandidatesCount = candidates.count(name) 
        #print(name)
        numberofVotersPerCandidates.append(CandidatesCount)
        PercentageCalculated = float(str(CandidatesCount))/float(str(TotalNumberofVotes))
        PercentageofVotersPerCandidates.append((PercentageCalculated)*100)
        tup = (name, PercentageCalculated*100, CandidatesCount)
        TupleList.append(tup)    
    
     #Display Output
    FilePrint.append("Election Results" + "\n" )
   
    FilePrint.append("---------------------------------------------" + "\n")
    FilePrint.append("Total Votes: " + str(TotalNumberofVotes) + "\n")

    FilePrint.append("---------------------------------------------" + "\n")
#Getting the Tuple list sorted and looping through to display the candidate list associated with their percentage of votes and providing the number of votes won per candidate.
TupleList.sort(key=lambda tup: tup[2], reverse=True)
for tup in TupleList:
    
    FilePrint.append(tup[0] + ": " + str(round(float(tup[1]),1)) + "%" + " " + " (" + str(tup[2]) + ")" + "\n")
Winner = TupleList[0][0] ## Access the first value in the tuplelist WinnerTup = TupleList[0]  
                                                                    # Winner = WinnerTup[0]

FilePrint.append("---------------------------------------------" + "\n")
FilePrint.append("Winner: " +  str(Winner) + "\n")

    
# Export a text file with the results.
with open(newfile, "w") as txtfile:
    #txtfile.write(str(("Election Results" )))
    txtfile.writelines(FilePrint)
    
        
    #txtfile.write('\n'.join(FilePrint) + '\n')
    #txtfile.writerows(FilePrint)
    #writer.writerow(["Index", "Employee", "Department"])

    #writer.writerows(roster)

#FinalResults.append(TupleList)

#print(TupleList)
#print(FinalResults)