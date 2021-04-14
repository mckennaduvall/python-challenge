import os
import csv
import numpy as np

#set path for file 
csvpath = os.path.join('Resources','PyPoll_Resources_election_data.csv')

# Lists to store data in
voter_ID = []
candidates = []
county = []


#open csv file
with open(csvpath, 'r') as csv_file:
	csv_reader = csv.reader(csv_file)

#add data into lists
	for line in csv_reader:

		voter_ID.append(line[0])
		total_votes = len(voter_ID)

		candidates.append(line[2])

		county.append(line[1])

#list to store unique names of candidates in
unique = []

#loop through candidates names
for candidate in candidates:

	if candidate not in unique:
		unique.append(candidate)


#lists to store number of votes
khan = []
correy = []
li = []
otooley = []

for candidate in candidates:

	if candidate == "Khan":

		khan.append(candidate)

		khan_votes = len(khan)

	if candidate == "Correy":

		correy.append(candidate)

		correy_votes = len(correy)

	if candidate == "Li":

		li.append(candidate)

		li_votes = len(li)

	if candidate == "O'Tooley":

		otooley.append(candidate)

		otooley_votes = len(otooley)


#calculate percent
total_count_candidates = len(candidates)

khan_percent = (khan_votes / total_count_candidates) * 100


correy_percent = (correy_votes / total_count_candidates) * 100

li_percent = (li_votes / total_count_candidates) * 100

otooley_percent = (otooley_votes / total_count_candidates) * 100


percentages = {'Khan':khan_percent, 'Correy':correy_percent, 'Li':li_percent,'otooley':otooley_percent}


winner = max(percentages, key=percentages.get)



txt_path =os.path.join('Analysis','pypoll.txt')

with open(txt_path, 'a') as f:

	f.write("Election Results")

	f.write("--------------------------")

	f.write(f"Total Votes: {total_votes}")

	f.write("--------------------------")

	f.write(f"Khan: {khan_percent}% ({khan_votes})")

	f.write(f"Correy:{correy_percent}% ({correy_votes})")

	f.write(f"Li: {li_percent}% ({li_votes})")

	f.write(f"O'Tooley: {otooley_percent}% ({otooley_votes})")

	f.write("--------------------------")

	f.write(f"Winner: {winner}")

	f.write("---------------------------")
