import os
import csv
import sys
# In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)
# You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

# Collect data from the Resources folder
csvpath = os.path.join("Resources", "election_data.csv")

# Define the lists that we will use
Candidates_list=[]
Count_votes_per_candidate=[]
Total_candidates_list=[]
Unique_candidates_list=[]
Votes_list=[]

# Read CSV file
with open(csvpath, newline='', encoding="utf8") as election_data:
 csvreader = csv.reader(election_data, delimiter=',')

 
 header = next(csvreader)

  #Loop through vote list and candidate list
 for row in csvreader:
     # Get the length of the votes list
     Votes_list.append(row[0])
     length = str(len(Votes_list))

     # Create a list of candidates
     Total_candidates_list.append(row[2])

 # Need to obtain how many times the candidates were voted for

 for i in Total_candidates_list:
     if i not in Unique_candidates_list:
         Unique_candidates_list.append(i)

 # Use comprehension list for total
 comprehension_list_total_count = [[x,Total_candidates_list.count(x)] for x in set(Total_candidates_list)]

 # Create a dictionary 
 summary_total_candidates = dict((x,Total_candidates_list.count(x)) for x in set(Total_candidates_list))

 # Obtain values and keys
 for key in summary_total_candidates:
     keys = key
 for value in summary_total_candidates.items():
     values = value

 
 # Create a list for the candidates and one for the votes
 for row in comprehension_list_total_count:
    Candidates_list.append(row[0])
    Count_votes_per_candidate.append(int(row[1]))

 # Obtain the max value of the list of votes.
 max_increase_value = max(Count_votes_per_candidate)
 max_increase_value_index = Count_votes_per_candidate.index(max_increase_value)
 winner = Candidates_list[max_increase_value_index]
print(" ")
print("Election Results")
print("-----------------------")
print(f"Total votes: {length}")
print("-----------------------")

for key, value in summary_total_candidates.items():
 print(f"{key}: {round((int(value)/int(length))*100)}% ({value})")
print("-----------------------")
print(f"Winner: {winner}")