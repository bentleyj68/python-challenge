# PyBank Analysis script - main.py
import os
import csv

# Function - Show results on screen and to a text file
#          - Input parameter is a dictionary of the analysis
def show_results(analysis_dict):
    # Specify the file to write the financial analysis result to
    output_path = os.path.join('analysis','results.txt')
    # Store each line in a list for reuse
    results = []
    results.append('Financial Analysis')
    results.append('-------------------------')
    results.append(f"Total Months: {analysis_dict['count']}")
    results.append(f"Total: {analysis_dict['net_profit']}")
    results.append(f"Avearge Change: {analysis_dict['average_difference']}")
    results.append(f"Greatest Increase in Profits: {analysis_dict['biggest_increase']}")
    results.append(f"Greatest Decrease in Profits: {analysis_dict['biggest_decrease']}")
    # Print the results to screen
    for result in results:
        print(result)
    # Open the file with write mode
    with open(output_path, 'w', newline='\n') as txtfile:
        # Print the results to a text file
        for result in results:
            txtfile.write(f"{result} \n")


# Main code - loop through csv file and calculate results
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
   
    # Read the header row first
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")
    
    # Setup a Python Dictionary to store all the results 
    analysis = {"count": 0,
                "net_profit":  0,
                "average_difference" :0,
                "biggest_increase": 0,
                "biggest_decrease": 0}

    for row in csvreader:
        analysis["count"] += 1
        analysis["net_profit"] = analysis["net_profit"] + int(row[1])
        # Ignore the first month when calculating the difference
        if analysis["count"] > 1:
            # Calculate the difference from the previous month
            difference = int(row[1]) - previous
            # Sum the differences from each month
            analysis["average_difference"] = analysis["average_difference"] + difference 
            # Check if the new difference is a bigger increase or decrease
            if difference > analysis["biggest_increase"]:
                analysis["biggest_increase"] = difference
            if difference < analysis["biggest_decrease"]:
                analysis["biggest_decrease"] = difference 
        # Store the current month for calculating the difference on the next month
        previous = int(row[1])

    # Use the sum of all differences to calculate the average, but ignore the first month
    analysis["average_difference"] = round(analysis["average_difference"] / (analysis["count"] -1), 2)
    # print(analysis)

    # Call the show_results function to display and store the results from the analysis
    show_results(analysis)