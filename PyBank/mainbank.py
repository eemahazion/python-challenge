import os

import csv

csvpath = os.path.join('C:/Users/emanu/repos/HW Challenges/python-challenge/PyBank/resources/budget_data.csv')
print("----------Bank Analysis----------")
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    data = list(csvreader)
    num_rows = len(data)
    print(f'The total number of months included in the dataset is {num_rows}')
    #the net total amount of profit/loss over entire period and then the average of those changes
    daily_income = [int(row[1]) for row in data]
    net_income = sum(daily_income)
    print(f'The total net income is ${net_income}')
    #for loop for average change in income
    prev_income = daily_income[0]
    changein_income =[]
    for income in daily_income[1:]:
        profit_change = income - prev_income
        changein_income.append(profit_change)
        prev_income = income
income_change = sum(changein_income)/len(changein_income)    
avground = round(income_change,2)
print(f"The average change in income was ${avground} daily")

#code for max and min profit amounts
max_increase_amount= 0
max_decrease_amount = 0
max_increase_month = ''
max_decrease_month= ''

previous_month = data[0][0]
current_month = ''

previous_month_amount = int(data[0][1])

for i in range(1,len(data)):
    row= data[i]
    current_month = row[0]
    current_month_amount = int(row[1])
    change = current_month_amount-previous_month_amount
    if change > max_increase_amount:
        max_increase_amount = change
        max_increase_month = row[0]
    if change < max_decrease_amount:
        max_decrease_amount = change
        max_decrease_month = row[0]
    previous_month_amount = current_month_amount
    previous_month = current_month
            
print(f"The greatest increase in profits was for the month of {max_increase_month} in the amount of ${max_increase_amount}")
print(f"The greatest decrease in profits was for the month of {max_decrease_month} in the amount of ${max_decrease_amount}")



#export output to a text file

text_output = os.path.join("C:/Users/emanu/repos/HW Challenges/python-challenge/PyBank/analysis", "bank_textfile.txt")

with open(text_output, 'w') as txto:
    txto.write(f'The total number of months included in the dataset is {num_rows}\n')
    txto.write(f'The total net income is ${net_income}\n')
    txto.write(f"The average change in income was ${avground} daily\n")
    txto.write(f"The greatest increase in profits was for the month of {max_increase_month} in the amount of ${max_increase_amount}\n"
               f"The greatest decrease in profits was for the month of {max_decrease_month} in the amount of ${max_decrease_amount}")