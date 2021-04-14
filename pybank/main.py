import os

import csv

#set path for file 
csvpath = os.path.join('Resources','budget_data.csv')

# Lists to store data
date = []
profit_losses = []
pl_changes = []

#open csv file
with open(csvpath, 'r') as csv_file:
	csv_reader = csv.reader(csv_file)

	next(csv_reader)

	for line in csv_reader:

#store data as lists
		date.append(line[0])
		profit_losses.append(int(line[1]))

#count number of months in list
		number_month = len(date)

#total the profit/losses list
		total = sum(profit_losses)

#loop through each number in profit/losses
	for i in range(len(profit_losses)-1):

		change = (profit_losses[i+1] - profit_losses[i])

		pl_changes.append(change)

		total_change = sum(pl_changes)

		number_change = len(pl_changes)

		max_change = max(pl_changes)

		min_change = min(pl_changes)

average_change = total_change / number_change


txt_path =os.path.join('Analysis','pybank.txt')

with open(txt_path, 'a') as f:

	f.write("Financial Analysis")

	f.write("-----------------------------------")

	f.write(f"Total Months: {number_month}")

	f.write(f"Total: ${total}")

	f.write(f"Average Change: ${average_change}")

	f.write(f"Greatest Increase in Profits: {max_change}")

	f.write(f"Greatest Decrease in Profits: {min_change}")


