#importing dependencies
import os
import csv

#specifying the file to read
budget_csv = os.path.join("Resources", "budget_data.csv")


#Opening and reading csv
with open(budget_csv) as csv_file:
    data = csv.reader(csv_file, delimiter=",")

# Reading the header row 
    csv_header = next(data)
    print(f"Header: {csv_header}")


    months = 0 
    total = 0
    prev_profit_loss = 0
    total_change=0
    greatest_increase=0
    greatest_increase_month=""
    greatest_decrease=0
    greatest_decrease_month=""

# getting the total months 
    for row in data:
        months += 1 
 
#getting the total profit/loss
        profit_loss = int(row[1])
        total += profit_loss

#getting the changes in profit/loss over time
        change = profit_loss - prev_profit_loss
        if prev_profit_loss == 0:
            change = 0
        total_change +=change
        prev_profit_loss=profit_loss

#getting the greatest increase in profit
        month= row[0]
        if change>greatest_increase:
            greatest_increase=change
            greatest_increase_month=month
        prev_profit_loss=profit_loss

#getting the greatest decrease in profit 
        if change<greatest_decrease:
            greatest_decrease=change
            greatest_decrease_month=month
        prev_profit_loss=profit_loss

#(PRINTING RESULT TO THE TERMINAL)
        
Result=f''' 
Financial Analysis
----------------------------
Total Months: {months}
Total: ${total}
Average Change: {total_change/(months-1):.2f}
Greatest Increase in Profits: { greatest_increase_month}  (${greatest_increase})
Greatest Decrease in Profits: {greatest_decrease_month}  (${greatest_decrease})

'''
print(Result)


#(EXPORTING RESULTS TO TEXT FILE )

#specifying the file to write to
output_file = os.path.join("Analysis","new.txt")


#initializing text writer
with open(output_file, "w") as datafile:

#writing results into the text file   
    datafile.write("Financial Analysis \n")
    datafile.write("------------------------\n")
    datafile.write(f"Total Months: {months}\n")
    datafile.write(f"Total: ${total}\n")
    datafile.write(f"Average Change: {total_change/(months-1):.2f}\n")
    datafile.write(f"Greatest Increase in Profits: { greatest_increase_month}  (${greatest_increase})\n")
    datafile.write(f"Greatest Decrease in Profits: {greatest_decrease_month}  (${greatest_decrease})")





