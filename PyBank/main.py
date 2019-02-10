import os
import csv
# Create the path
csvpath = os.path.join(".", "Resources", "budget_data.csv")

# Create a list to store values
total_months = []
total_profit_losses = []
change_profit_losses = []

# Open the csv file
with open(csvpath,newline="", encoding="utf-8") as budget_data:

# Store the contents of the csv
    csvreader = csv.reader(budget_data,delimiter=",")
# Remove the header
    header = next(csvreader)
# iterate through rows to fill the lists created
    for row in csvreader:
        total_months.append(row[0])
        total_profit_losses.append(int(row[1]))

# iterate through the profit losses list to get monthly change
for i in range(len(total_profit_losses)-1):
# Take the difference between two months
    change_profit_losses.append(total_profit_losses[i+1]-total_profit_losses[i])

# Obtain the greatest increase in profits over the period
max_increase_value = max(change_profit_losses)
max_increase_month = change_profit_losses.index(max(change_profit_losses)) + 1
# Obtain the greatest decrease over the period
max_decrease_value = min(change_profit_losses)
max_decrease_month = change_profit_losses.index(min(change_profit_losses)) + 1

# Print with the proper format
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: $ {sum(total_profit_losses)}")
print(f"Average Change: {round(sum(change_profit_losses)/len(change_profit_losses),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} $ {(str(max_increase_value))}")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} $ {(str(max_decrease_value))}")

