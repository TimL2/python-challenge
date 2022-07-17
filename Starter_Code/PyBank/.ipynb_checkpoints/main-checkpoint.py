#PyBank Assignment - Tim Lukes
#Import csv lib
from pathlib import Path
import csv

#Set Filepath
csvpath = Path('Resources/budget_data.csv')

# Initialize csv navigation variables
line_num = 0
profits = []
dates = []
changes = []

#Initialize math variables
total_months = 0
total_profit = 0
average_profit = 0
average_change = 0
total_change = 0
change_count = 0
max_profit = 0
max_profit_date = ""
min_profit = 0
min_profit_date = ""
prev_profit = 0

# Open the input path as a file object
with open(csvpath, 'r') as csvfile:

    # Pass in the csv file to the csv.reader() function
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Assign Header
    header = next(csvreader)
    line_num += 1
    
    # Print the header
    #print(f"{header} <---- HEADER")
    
    # Read each row of data after the header
    for row in csvreader:
        #print(row)
        profit = int(row[1])
        profits.append(profit)
        date = str(row[0])
        dates.append(date)
        change = profit - prev_profit
        if csvreader.line_num > 2:
            changes.append(change)
            total_change += change
            change_count += 1
            
        #Add 1 to month count
        total_months += 1
        
        #Add profit to total_profit
        total_profit += profit
        
        #Check for max profit and min profit
        if change > max_profit:
            max_profit = change
            max_profit_date = date
        elif min_profit == 0:
            min_profit = change
            min_profit_date = date
        elif change < min_profit:
            min_profit = change
            in_profit_date = date
        prev_profit = profit
        
    #Calc average profit
    average_profit = (total_change / change_count)

#Display Results
print()
print("Financial Analysis")
print()     
print("----------------------------")
print()
print(f'Total Months: {total_months}')
print()
print(f'Total: ${total_profit}')
print()
print(f'Average Change: ${round(average_profit,2)}')
print()
print(f'Greatest Increase in Profits: {max_profit_date} ${max_profit}')
print()
print(f'Greatest Increase in Profits: {min_profit_date} ${min_profit}')

# Set the output header
header = ["total_months", "total_profit", "average_profit", "max_profit", "max_profit_date", "min_profit", "min_profit_date"]
# Create a list of metrics
metrics = [total_months, total_profit, average_profit, max_profit, max_profit_date, min_profit, min_profit_date]

# Set the output file path
output_path = Path('output.csv')

# Open the output path as a file object
with open(output_path, 'w') as csvfile:
    # Set the file object as a csvwriter object
    csvwriter = csv.writer(csvfile, delimiter=',')
    # Write the header to the output file
    csvwriter.writerow(header)
    # Write the list of metrics to the output file
    csvwriter.writerow(metrics)

