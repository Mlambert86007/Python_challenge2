#In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.
#You will be given a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following:
#* The total number of votes cast
#* A complete list of candidates who received votes
# The percentage of votes each candidate won
#* The total number of votes each candidate won
#* The winner of the election based on popular vote.
#Your analysis should look similar to the following:
#  ```text
#  Election Results
#  -------------------------
# Total Votes: 369711
# -------------------------
 # Charles Casper Stockham: 23.049% (85213)
  #Diana DeGette: 73.812% (272892)
  #Raymon Anthony Doane: 3.139% (11606)
  #-------------------------
  #Winner: Diana DeGette
  #-------------------------
  #```
#In addition, your final script should both print the analysis to the terminal and export a text file with the results.

#Begin Task
import os
import csv


#set path for file to read
csvreader = os.path.join('Resources', 'election_data.csv')

# Set up the text file
txtwriter = os.path.join('analysis', 'election_data.txt')

#create lists to store data
candidate_list = []
Ballot_ID = []
County = []
Vote_total = []
county_name = []
votes_by_candidate = {}
candidate_name = []
winner = 0
wpercentage = 0
votes = 0


#With Fingers Crossed, Lets begin!

# opening the Reader
with open(csvreader) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #Take out the header
    csvheader = next(csvreader)
    
    #"For" Loop, Let's get some data going!
    for row in csvreader:
        #setup first numbers
        candidate_name = row[2]
        county_name.append(row[1])

        # Add Ballots (total number of votes)
        Ballot_ID.append(row[0])

        #get all the candiates unique names--This took forever too.  I wish I was smarter
        if candidate_name not in candidate_list:
            #add in the name
            candidate_list.append(candidate_name)
            #start the vote count
            votes_by_candidate[candidate_name] = 0
        #add the votes for that candidate
        votes_by_candidate[candidate_name] +=1

#Vote Totals--Honestly I think this was a rather clever way of doing this    
vote_total = len(Ballot_ID)

# Lets start writing data to our text file
with open(txtwriter, "w") as txt_file:
    
    # Lets print the final vote count, man figuring out the \n took longer than it should
    election_total_results = (
        f"\nElection Results\n" f"-------------------------\n" f"Total Votes: {vote_total:,}\n" f"-------------------------\n")

    print(election_total_results, end=" ")

# Lets save the final vote count into our text file
    txt_file.write(election_total_results)

    for candidate in votes_by_candidate:
        
        # Retrieve vote count and percentage.
        votes = votes_by_candidate[candidate]
        vote_percentage = float(votes) / float(vote_total) * 100
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        #  Save the candidate results to the text file.
        txt_file.write(candidate_results)

        # Print all the candidate's results
        print(candidate_results)
        

        
    # Ok, after much frustration above... Lets figure out the winning vote count, winning percentage, and winning candidate.
        if (votes > winner) and (vote_percentage > wpercentage):
                winner = votes
                winning_candidate = candidate
                winning_percentage = vote_percentage
    
    
     # Print the winning candidates name--this was easy.  Note to self...separate the printing
     #Dont try to do it all at once. #thatwasallsaturday
    winning_candidate_name = (f"-------------------------\n" f"Winner: {winning_candidate}\n" f"-------------------------\n")
    print(winning_candidate_name)
    
    # WOW! We finally got this one! Save the winning candidate's results to our text file. Fini!
    txt_file.write(winning_candidate_name)




