import csv
import os
#file path
budget_data = r"Python_challenge\python-challenge\PyBank\Resources\budget_data.csv"

#storing variabls
unique_months = set()
previous_value = None
net_changes = 0
comparison = 0
greatest_increase = ("",0)
greatest_decrease = ("",0)
every_change = [] 

#reading csv file
with open(budget_data, newline= "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #skip header
    next(csvreader)

    #going over every row
    for row in csvreader:
        
        #extracting data
        #finding total months
        month = row[0]
        unique_months.add(month)
        total_months = len(unique_months)

        #net total
        change = float(row[1])
        net_changes += change

        #greatest increase + decrease
        current_value = int(row[1])
        
        if previous_value is not None:
            comparison = current_value - previous_value
            #append comparisons
            every_change.append(comparison)

            if comparison > greatest_increase[1]:
                greatest_increase = (month, comparison)
            elif comparison < greatest_decrease[1]:
                greatest_decrease = (month, comparison)
        previous_value = current_value
# average change of profit/losses
average_change = round(sum(every_change) / total_months, 2)

#printing results!
print("Financial Analysis")
print("----------------------------")
print("Total Months:", total_months) 
print("Total:", round(net_changes, 0))
print("Average Change:", round(average_change, 2))
print("Greatest Increase in Profits:", greatest_increase[0], "($", greatest_increase[1], ")")
print("Greatest Decrease in Profits:", greatest_decrease[0], "($", greatest_decrease[1], ")")

# exporting as text file
os.chdir("Python_challenge\python-challenge\PyBank")
with open("main.py", "r") as python_file:
    python_code = python_file.read()
with open("Exported text File of Main.py", "w") as export_file:
    export_file.write(python_code)