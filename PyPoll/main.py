#dependencies

# Module for reading CSV files
import os
import csv

csvpath = "/Users/adesolafakiyesi/Desktop/python_challenge/PyPoll/Resources/election_data.csv" 

# # Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))

total_votes = 0 
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0
# Method 2: Improved Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

  

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    for row in csvreader: 
    # Calculate the total number of votes cast)
        total_votes += 1
    # Calculate the total number of votes of each candidate)
        if (row[2] == "Khan"):
           khan_votes += 1
        elif (row[2] == "Correy"):
            correy_votes +=1
        elif (row[2] == "Li"):
            li_votes +=1
        else:
            otooley_votes +=1

    # Calculate Percentage of votes of each candidate
    khan_percent = khan_votes / total_votes
    correy_percent = correy_votes / total_votes
    li_percent = li_votes / total_votes
    otooley_percent = otooley_votes / total_votes

    # Calculate winner of the election based on popular vote
    winner = max (khan_votes, correy_votes, li_votes, otooley_votes)

    if winner == khan_votes:
       winner_name = "khan"
    elif winner == correy_votes:
         winner_name = "correy"
    elif winner == li_votes:
         winner_name = "li"
    else:
        winner_name = "otooley"

# Print Summary Analysis
print(f"Election Results")
print(f"---------------------------")
print(f"Total Votes: {total_votes}")
print(f"---------------------------")
print(f"Khan: {khan_percent:.3%}({khan_votes})")
print(f"Correy: {correy_percent:.3%}({correy_votes})")
print(f"Li: {li_percent:.3%}({li_votes})")
print(f"O'Tooley: {otooley_percent:.3%}({otooley_votes})")
print(f"---------------------------")
print(f"Winner: {winner_name}")
print(f"---------------------------")

# Specify file to write to

output_path = os.path.join( "PyPoll", "Analysis", "election_analysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:

   
    # Write new data
    txtfile.write(f"Election Results\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Khan: {khan_percent:.3%}({khan_votes})\n")
    txtfile.write(f"Correy: {correy_percent:.3%}({correy_votes})\n")
    txtfile.write(f"Li: {li_percent:.3%}({li_votes})\n")
    txtfile.write(f"O'Tooley: {otooley_percent:.3%}({otooley_votes})\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Winner: {winner_name}\n")
    txtfile.write(f"---------------------------\n")
    

 