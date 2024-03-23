#!/usr/bin/env python
# coding: utf-8

# In[7]:


import os
import csv


# In[8]:


path_input = os.path.join("Resources", "election_data.csv")
path_output = os.path.join("Analysis", "election_data_result.csv")


# In[9]:


# Define variables
# Dictionary of dictionaries: for each key there is a values and this value is a dictionary
all_voters = {}

# Set for candidates
candidates = set()

# Dictionary for votes for each candidate
candidate_votes = {}
candidate_percent = {}

# Read from csv file
with open(path_input, "r") as csv_file:
    #-- use csv.DictReader to have iterable object each element of which is a dictionary    
    csv_reader = csv.DictReader(csv_file, delimiter = ',')

    #---Read data from file, fill Candidates set, and all_voters dictionary {voter_ID : candidate_name}
    for row in csv_reader:
        candidates.add(row['Candidate'])        
        all_voters[row['Voter ID']] = row['Candidate']

    #---Add data to candidates_votes dictionary {candidate_name : 0}, candidates_percent dictionary {candidate_name : 0.0}
    for candidate in candidates:
       candidate_votes[candidate] = 0
       candidate_percent[candidate] = 0.0
    
    #---Calculate number of votes for each candidate
    for voter in all_voters.items():
        for cand in candidates:
          if cand == voter[1]:
            candidate_votes[cand] += 1 
    
    #---Calculate percentage of votes for each candidate and define the winner
    winner_scores = 0
    total_votes = len(all_voters)
    for candidate in candidate_votes.items():
        candidate_percent[candidate[0]] = round(candidate[1]/total_votes, 2)
        #---Define the winner
        if candidate[1] > winner_scores:
            winner_name = candidate[0]
            winner_scores = candidate[1]
           

'''   
    for row in csv_reader:
        
        # Save poll data to Dictionary with Key - Voter ID: value - Dictionary with voter ID, values for County and Candidate
        all_voters[row['Voter ID']] = row
        
        #---Find a complete list of candidates who received votes. Set() structure contains only unique values
        candidates.add(row['Candidate'])

    #-------Calculate the total number of votes cast
    total_votes = len(all_voters)
    
    #-------Calculate votes and percentage of votes for each candidate and define the winner
    max_value = 0.0
    for candidate in candidates:
        
        count_votes = 0    
        # Count votes for each candidates
        for voter in all_voters.values():
            if voter['Candidate'] == candidate:
                count_votes += 1
                
        # Add Dictionaries with Key - candidate name : Value - tuple with total votes and perentage of votes       
        candidate_votes[candidate] = (round(count_votes/total_votes, 2), count_votes)

        #---Define the winner
        if candidate_votes[candidate][0] > max_value:
            winner_name = candidate
            max_value = candidate_votes[candidate][0]
            
'''

# Analysis output---------------------------------------------------------------------------------------------
    
header_row = f"Election Results \n--------------------\nTotal votes: {total_votes} \n--------------------"
winner_row = f"\n--------------------\nWinner: {winner_name} \n--------------------"
    
# Print the analysis in the terminal 
print(header_row)
    
for each in sorted(candidates):
    #print(f'{each}:\t{"{:.2%}".format(candidate_votes[each][0])} ({candidate_votes[each][1]})')
    print(f'{each}:\t{"{:.2%}".format(candidate_percent[each])} ({candidate_votes[each]})')
    
print(winner_row)

    
# Save the analysis to the text file
with open(path_output, 'w') as csv_file:  
    csv_writer = csv.writer(csv_file, delimiter = ',')
    
    csv_writer.writerow([header_row])
    
    for each in sorted(candidates):
        #csv_writer.writerow([f'{each}:\t{"{:.2%}".format(candidate_votes[each][0])} ({candidate_votes[each][1]})'])
        csv_writer.writerow([f'{each}:\t{"{:.2%}".format(candidate_percent[each])} ({candidate_votes[each]})'])

    csv_writer.writerow([winner_row])
    


# In[ ]:




