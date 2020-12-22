import os
import csv

file_path = os.path.join("./", "Resources", "election_data.csv")
# print(file_path)

# Create an empty dictionary to store election result
election_result = {}
# Create an empty set to store voters
voter_sets = set()
repeat_voters = set()

# Initiate election_result
election_result["total_votes"] = 0
election_result["candidates"] = set()
election_result["results"] = {}

with open(file_path, "r") as csv_file:
  csv_reader_obj = csv.reader(csv_file, delimiter=",")

  # Retrieve the header and move the pointer to next line
  file_header = next(csv_reader_obj)
  # print(file_header)

  for row in csv_reader_obj: 
    if row[0] not in voter_sets:
      voter_sets.add(row[0])
      election_result["total_votes"] += 1
      if row[2] not in election_result["candidates"]:
        election_result["candidates"].add(row[2])
        new_obj = {}
        new_obj["name"] = row[2]
        new_obj["vote_count"] = 1
        election_result["results"][row[2]] = new_obj
      else:
        election_result["results"][row[2]]["vote_count"] += 1 
    else:
      repeat_voters.add(row[0])


print(len(voter_sets))
print(election_result)


