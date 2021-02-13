# ## PyPoll

# ![Vote Counting](Images/Vote_counting.png)

# * In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.

# * You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

#   * The total number of votes cast

#   * A complete list of candidates who received votes

#   * The percentage of votes each candidate won

#   * The total number of votes each candidate won

#   * The winner of the election based on popular vote.

# * As an example, your analysis should look similar to the one below:

#   ```text
#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------
#   ```

# * In addition, your final script should both print the analysis to the terminal and export a text file with the results.

import os
import csv

# create variables
vote_total = 0
khan_vote = 0
correy_vote = 0
li_vote = 0
otooley_vote = 0


##READ IN CSV FILE
# import csv data

csvpath = os.path.join('Resources', 'election_data.csv')

#   read in the data line by line
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

# Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

##ORGANIZE DATA IN PYTHON

    #go through each row
    for row in csvreader:
            
        #count the total votes
        vote_total +=1
            
        #count number of votes for each candidate
        if row[2] == "Khan":
                khan_vote += 1
        elif row[2] == "Correy":
                correy_vote +=1
        elif row[2] == "Li":
                li_vote +=1
        elif row[2] == "O'Tooley":
                otooley_vote +=1


##CALCULATIONS
#Create lists using the newly gathered vote counts
candidates = ["Khan", "Correy", "Li", "O'Tooley" ]
votes = [khan_vote, correy_vote, li_vote, otooley_vote]

#Use zip to create a dictionary of candidates and their votes
vote_count_dict = dict(zip(candidates, votes))

#find winner using max
winner = max(vote_count_dict, key=vote_count_dict.get)

#Store the percentages of votes
khan_percentage = (khan_vote/vote_total) *100
correy_percentage = (correy_vote/vote_total) *100
li_percentage = (li_vote/vote_total)*100
otooley_percentage = (otooley_vote/vote_total)*100
            


# PRINT RESULTS TO TERMINAL
# for each item in candidate info
#   print candidate, total votes won, percentage votes won
# print winner based on popular vote

print("Election Results!")
print("----------------------------")
print(f"Total Votes: {vote_total}")
print("----------------------------")
print(f"Khan: {khan_percentage:.2f}% ({khan_vote})")
print(f"Correy: {correy_percentage:.2f}% ({correy_vote})")
print(f"Li: {li_percentage:.2f}% ({li_vote})")
print(f"O'Tooley': {otooley_percentage:.2f}% ({otooley_vote})")
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")


# EXPORT RESULTS 
# export above results to a text file by using csv.write
output_path = os.path.join("Analysis", "Election_Results.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:
    
  csvfile.write("Election Results!")
  csvfile.write("\n")
  csvfile.write("----------------------------")
  csvfile.write("\n")
  csvfile.write(f"Total Votes: {vote_total}")
  csvfile.write("\n")
  csvfile.write("----------------------------")
  csvfile.write("\n")
  csvfile.write(f"Khan: {khan_percentage:.2f}% ({khan_vote})")
  csvfile.write("\n")
  csvfile.write(f"Correy: {correy_percentage:.2f}% ({correy_vote})")
  csvfile.write("\n")
  csvfile.write(f"Li: {li_percentage:.2f}% ({li_vote})")
  csvfile.write("\n")
  csvfile.write(f"O'Tooley': {otooley_percentage:.2f}% ({otooley_vote})")
  csvfile.write("\n")
  csvfile.write("----------------------------")
  csvfile.write("\n")
  csvfile.write(f"Winner: {winner}")
  csvfile.write("\n")
  csvfile.write("----------------------------")  



