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

# create empty dictionary called candidate_info
candidate_info = {}


##READ IN CSV FILE
# import csv data

csvpath = os.path.join('Resources', 'election_data.csv')

#   read in the data line by line
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

# Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

##ORGANIZE DATA IN PYTHON

# iterate through each row of csvdata
    for row in csvreader:
#   if the candidate (row[2]) is not equal to a key in candidate_info
        if (row[2]) != candidate_info:            
#       add candidate as new key with empty integer value
            candidate_info[row[2]] = int(0) 
#       add 1 to integer value
        elif (row[2]) == candidate_info:
             candidate_info[row] = (int(0) + 1)
#   else (meaning, if the candidate already exists in our dictionary)
        else:
#       add 1 to matching integer value
            
##CALCULATIONS
# sum of each candidate total = total votes
# candidate total/total votes = percent won
# PRINT RESULTS TO TERMINAL
# for each item in candidate info
#   print candidate, total votes won, percentage votes won
# print winner based on popular vote
# EXPORT RESULTS 
# export above results to a text file by using csv.write    
