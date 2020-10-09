#dependencies
import os
import csv

total_months = 0 
prev_revenue = 0
revenue_change_list = []
greatest_increase = ['', 0]
greatest_decrease = ['', 9999999999999999999999]
total_revenue = 0

csvpath = os.path.join("Resources", "budget_data.csv")
#csvpath = "/Users/adesolafakiyesi/Desktop/python_challenge/PyBank/Resources/budget.data.csv"

# Read csv and convert to a list of dictionaries
with open(csvpath) as revenue_data:
	csvreader = csv.reader(revenue_data,  delimiter=',')
	
	# Get header so it doesn't disrupt calculations
	header = next(csvreader)
	
	# Get first row and make first calculations to initialize for the rest of calculations
	first_line = next(csvreader)
	total_months += 1
	prev_revenue = int(first_line[1])
	total_revenue += prev_revenue

	for row in csvreader:

		# Calculate total number of months & revenue
		total_months += 1
		total_revenue += int(row[1])

		# Calculate revenue change
		revenue_change = int(row[1]) - prev_revenue
		prev_revenue = int(row[1])
		revenue_change_list.append(revenue_change)
		
		if greatest_decrease[1] > revenue_change:
			greatest_decrease[0] = row[0]
			greatest_decrease[1] = revenue_change
		if greatest_increase[1] < revenue_change:
			greatest_increase[0] = row[0]
			greatest_increase[1] = revenue_change


 # Calculate average revenue change
revenue_average = sum(revenue_change_list)/ len(revenue_change_list) 

# Print Summary Analysis
output = (f"Financial Analysis" 
	f"\n---------------------------"
	f"\nTotal Months: {total_months}"
	f"\nTotal Revenue: ${total_revenue}"
	f"\nAverage Revenue Change: ${revenue_average}"
	f"\nGreatest Increase in Profits: {greatest_increase[0]}, (${greatest_increase [1]})"
	f"\nGreatest Decrease in Profits: {greatest_decrease[0]}, (${greatest_decrease [1]})")

print(output)

# Specify file to write to
output_path = os.path.join("Analysis", "budget_data_analysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:
	txtfile.write(output)


