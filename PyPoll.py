import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize total vote counter.
total_votes = 0

# Declare Candidate options
candidate_options = []
# 1. Declare empty dictionary.
candidate_votes = {}

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row
    for row in file_reader:
        # Add total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        if candidate_name not in candidate_options:

          # Add the candidate name to candidate list.
            candidate_options.append(candidate_name)

            # Track candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to candidates count
        candidate_votes[candidate_name] += 1

#Determine percentage of votes by looping through counts
# Iterate through candidate list
for candidate_name in candidate_votes:
    #Retrieve vote count of candidate
    votes = candidate_votes[candidate_name]
    #Calculate percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100
   
#Print out candidates names, vote count, and percentage of votes
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

   #Determine if votes is greater than winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
       # if true then set winning_count = votes & winning_percent = vote_percentage
       winning_count = votes
       winning_percentage = vote_percentage
       # set the winning_candidate equal to candidates name
       winning_candidate = candidate_name

winning_candidate_summary = (
f"Winner: {winning_candidate}\n"
f"Winning Vote Count: {winning_count:,}\n"
f"Winning Percentage: {winning_percentage:.1f}%\n"
f"------------------------\n")

print(winning_candidate_summary)
