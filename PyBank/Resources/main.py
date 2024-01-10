import os
import csv

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Set the path to the CSV file
csv_path = os.path.join("..","Resources", "budget_data.csv")

# Initialize variables
total_months = 0
net_total = 0
previous_profit_loss = 0
changes = []
dates = []

# Read the CSV file
with open(csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)  # Skip header row

    # Iterate through the rows in the CSV
    for row in csvreader:
        # Extract date and profit/loss from the row
        date = row[0]
        profit_loss = int(row[1])

        # Calculate total profit/loss
        net_total += profit_loss

        # Calculate changes in profit/loss
        if total_months > 0:
            change = profit_loss - previous_profit_loss
            changes.append(change)
            dates.append(date)

        # Update previous profit/loss for the next iteration
        previous_profit_loss = profit_loss

        # Increment total months
        total_months += 1

# Calculate average change
average_change = sum(changes) / len(changes)

# Find the greatest increase and decrease in profits
greatest_increase = max(changes)
greatest_decrease = min(changes)

# Find the corresponding dates for greatest increase and decrease
increase_date = dates[changes.index(greatest_increase)]
decrease_date = dates[changes.index(greatest_decrease)]

# Set the path to the analysis folder
analysis_folder = os.path.join(script_dir, "analysis")

# Ensure the analysis folder exists
os.makedirs(analysis_folder, exist_ok=True)

# Set the path to the output text file
output_file_path = os.path.join(analysis_folder, "financial_analysis.txt")

# Write results to the text file
with open(output_file_path, "w") as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("--------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${net_total}\n")
    output_file.write(f"Average Change: ${average_change:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {increase_date} (${greatest_increase})\n")
    output_file.write(f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})\n")

# Print results to the console
with open(output_file_path, "r") as output_file:
    print(output_file.read())

print("Analysis complete. Results saved to financial_analysis.txt.")
