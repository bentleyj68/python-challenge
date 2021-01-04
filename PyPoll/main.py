# PyPoll election results script - main.py
import os
import csv

# Function - Show results on screen and write to a text file
#          - Input parameter is a dictionary of the analysis
def show_results(final_rslt):
    
    # Specify the file to write the financial analysis result to
    output_path = os.path.join('analysis','results.txt')
    
    # Store each line in a list for reuse
    results = []
    results.append('Election Results')
    results.append('------------------------------')
    results.append(f"Total Votes: {final_rslt['count']}")
    results.append('------------------------------')

    for i in range(len(final_rslt["candidate"])):
        results.append(f"{final_rslt['candidate'][i]}: {final_rslt['candidate_percent'][i]}% ({final_rslt['candidate_count'][i]})")
        
    results.append('------------------------------')
    results.append(f"Winner: {final_rslt['winner']}")
    results.append('------------------------------')

    # Print the results to screen
    for result in results:
        print(result)
    
    # Open the file with write mode
    with open(output_path, 'w', newline='\n') as txtfile:
        # Print the results to a text file
        for result in results:
            txtfile.write(f"{result} \n")

# Main code - loop through csv file and calculate results
csvpath = os.path.join('Resources', 'election_data.csv')

# Setup a Python Dictionary to store all the results 
analysis = {"count": 0,
            "candidate":  [],
            "candidate_percent":  [],
            "candidate_count":  [],
            "winner": ""}

most_votes = 0

with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
   
    # Read the header row first and ignore it
    csv_header = next(csvreader)

    # loop through the csv and calculate the analysis
    for row in csvreader:
        # count the total votes
        analysis["count"] += 1
        # check if candidate is new in the list and add to their votes
        if row[2] in analysis["candidate"]:
            index = analysis["candidate"].index(row[2])
            analysis["candidate_count"][index] += 1
        else:
            analysis["candidate"].append(row[2])
            analysis["candidate_count"].append(1)

    # work through each candidate in the list and calculate vote percentage
    for i in range(len(analysis["candidate"])):
        analysis["candidate_percent"].append('{:.3f}'.format(round(analysis["candidate_count"][i] / analysis["count"] * 100, 2)))
        # find the winner
        if analysis["candidate_count"][i] > most_votes:
            analysis["winner"] = analysis["candidate"][i]
            most_votes = analysis["candidate_count"][i]

# Call the show_results function to display and store the results from the analysis
show_results(analysis)