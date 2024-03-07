import csv

#file path
budget_data = r"C:\Users\Owner\Desktop\DA Classwork\M3 Starting Python yay\Python_challenge\python-challenge\PyBank\Resources\budget_data.csv"

#storing variabls
unique_months = set()
net_total = 0
net_changes = 0
greatest_increase = 0
greatest_decrease = 0

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
        change = int(row[1])
        net_changes += change
        #changes in profit/losses over entire period(average change)


        #greatest increase + decrease
        if change > greatest_increase:
            greatest_increase = change
        elif change < greatest_decrease:
            greatest_decrease = change




print({total_months})
print({net_changes})
print({greatest_increase})
print({greatest_decrease})