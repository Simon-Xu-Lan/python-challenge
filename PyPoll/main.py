import os
import csv

file_path = os.path.join("./", "Resources", "election_data.csv")
# print(file_path)

# Create an empty dictionary to store election result
election_result = {}

# Initiate election_result
election_result["total_votes"] = 0
election_result["candidates"] = {}
election_result["winner"] = {}
winner_votes = 0

with open(file_path, "r") as csv_file:
  csv_reader_obj = csv.reader(csv_file, delimiter=",")

  # Retrieve the header and move the pointer to next line
  file_header = next(csv_reader_obj)
  total_votes = 0
  for row in csv_reader_obj: 
    # row[0]: Voter, row[2]: Candidate
    election_result["total_votes"] += 1
    if row[2] not in election_result["candidates"]:
      # If row[2] is not key of election_result["candidates"], add it as new key
      # create a new object as value
      new_obj = {}
      new_obj["vote_count"] = 1
      election_result["candidates"][row[2]] = new_obj
    else:
      # If row[2] is a key of election_result["candidates"], add 1 to its value
      election_result["candidates"][row[2]]["vote_count"] += 1 

# Calculate percentage and winner
total = election_result["total_votes"]
winner = ""
highest_votes = 0
for candidate in election_result["candidates"]:
  votes = election_result["candidates"][candidate]["vote_count"]
  percentage = f"{round(votes / total * 100, 3)}00%"
  election_result["candidates"][candidate]["percentage"] = percentage
  if votes > highest_votes:
    highest_votes = votes
    winner = candidate
election_result["winner"] = winner

# Create string for candidnate data
# Using for loop inside f-string
candidate_data_str = "\n".join(f"{key}: {value['percentage']} ({value['vote_count']})" for key, value in election_result['candidates'].items())

# Create result string to print and save
result = f"\
Election Results\n\
-------------------------\n\
Total Votes: {total}\n\
-------------------------\n\
{candidate_data_str}\n\
-------------------------\n\
Winner: {election_result['winner']}\n\
-------------------------\n\
"

print(result)

# Write the result to txt file
with open("PyPoll_result.txt", "w") as file:
  file.write(result)
