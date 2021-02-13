#   * The greatest increase in profits (date and amount) over the entire period

#   * The greatest decrease in losses (date and amount) over the entire period

# * As an example, your analysis should look similar to the one below:

#   ```text
#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)
#   ```

# * In addition, your final script should both print the analysis to the terminal and export a text file with the results.

import os
import csv


csvpath = os.path.join('Resources', 'budget_data.csv')


total_money = []
month_count = []
monthly_money = []

with open(csvpath) as csvfile:

# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

# Read the header row first 
    csv_header = next(csvreader)
   
        
#   * The total number of months included in the dataset
    for row in csvreader:
        month_count.append(row[0])
        total_money.append(int(row[1]))
        
        total_months = len(month_count)

#   * The net total amount of "Profit/Losses" over the entire period  
    for i in range(len(total_money)-1):
        
#   * Calculate the changes in "Profit/Losses" over the entire period 
        monthly_money.append(total_money[i+1]-total_money[i])
  
        total_amount = sum(total_money)
#   find the average of those changes
        avg_change = round(sum(monthly_money)/len(monthly_money), 2)
    

# grab the max profit
max_value = max(monthly_money)
    
# grab the minimum profit
min_value = min(monthly_money)


# find the month associated with the min/max value
max_month = monthly_money.index(max(monthly_money)) + 1
min_month = monthly_money.index(min(monthly_money)) + 1

increase_month = month_count[max_month]
decrease_month = month_count[min_month] 
    


print('Financial Analysis')
print('------------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${total_amount}')
print(f'Average Change: {avg_change}')
print(f'Greatest Increase in Profits: {increase_month} {max_value}')
print(f'Greatest Decrease in Profits: {decrease_month} {min_value}')

# * In addition, your final script should both print the analysis to the terminal and export a text file with the results.
## WRITE OUTPUT
# Specify the file to write to
output_path = os.path.join("Analysis", "Financial_Summary.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    csvfile.write('Financial Analysis')
    csvfile.write("\n")
    csvfile.write('------------------------------')
    csvfile.write("\n")
    csvfile.write(f'Total Months: {total_months}')
    csvfile.write("\n")
    csvfile.write(f'Total: ${total_amount}')
    csvfile.write("\n")
    csvfile.write(f'Average Change: {avg_change}')
    csvfile.write("\n")
    csvfile.write(f'Greatest Increase in Profits: {increase_month} {max_value}')
    csvfile.write("\n")
    csvfile.write(f'Greatest Decrease in Profits: {decrease_month} {min_value}')
    
   

















    
    