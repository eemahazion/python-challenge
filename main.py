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

#Elections Analysis

import os

import csv

election_csvpath = os.path.join('C:/Users/emanu/repos/HW Challenges/python-challenge/PyPoll/resources/election_data.csv')
print("----------Elections Analysis----------")

with open(election_csvpath) as election_csvfile:
    elect_csvreader = csv.reader(election_csvfile, delimiter=',')
    total_election_data = list(elect_csvreader)
    #HEADER FOR ELECTION DATA
    election_header = total_election_data[:1]
    #Data only (w/0 headers)
    election_data = total_election_data[1:]
    election_data
    print(f" The amount of votes casted was {len(election_data)}")
    list_candidate = []

    for i in election_data:
    #     election_candidate = election_data[0]
    #     list_candidate += election_candidate + ','
        if i[2] not in list_candidate:
            list_candidate.append(i[2])
            
print(f"Candidates on the ballot were {list_candidate[0]}, {list_candidate[1]}, and {list_candidate[2]}")

#adding each candidates name in a respective list
#then will divide by total votes to get percentage for candidate

charles_vote = []
diana_vote =[]
raymon_vote = []

for i in election_data:
    if i[2] == "Charles Casper Stockham":
        charles_vote.append(i)
    if i[2] == "Diana DeGette":
        diana_vote.append(i)
    if i[2] == "Raymon Anthony Doane":
        raymon_vote.append(i)


#displaying the total number of votes each candidate won and calculation percentage won
print(f"The vote count was as follows: "
      f"{list_candidate[0]} with {len(charles_vote)}, "
      f"{list_candidate[1]} with {len(diana_vote)}, "
      f"and {list_candidate[2]} with {len(raymon_vote)}")

charles_results = len(charles_vote)/len(election_data)
diana_results = len(diana_vote)/len(election_data)
raymon_results = len(raymon_vote)/len(election_data)
#round the decimals
c_rounded = round(charles_results,5)
d_rounded = round(diana_results,5)
r_rounded = round(raymon_results,6)

#print final results
print(f"The election results were as follows: "
      f"{list_candidate[0]} with {(c_rounded)*100:.3f}%, "
      f"{list_candidate[1]} with {(d_rounded)*100:.3f}%, "
      f"{list_candidate[2]} with {(r_rounded)*100:.3f}%")

print(f'Winner is {list_candidate[1]}')

#export output to a text file

text_output = os.path.join("C:/Users/emanu/repos/HW Challenges/python-challenge/PyPoll/analysis/", "election_textfile.txt")
with open(text_output, 'w') as txto:
    txto.write(f" The amount of votes casted was {len(election_data)}\n")
    txto.write(f"Candidates on the ballot were\n {list_candidate[0]}\n {list_candidate[1]}\n and {list_candidate[2]}\n")
    txto.write(f"The vote count was as follows: \n"
      f"{list_candidate[0]} with {len(charles_vote)}, \n"
      f"{list_candidate[1]} with {len(diana_vote)}, \n"
      f"and {list_candidate[2]} with {len(raymon_vote)}\n")
    txto.write(f"The election results were as follows: \n"
      f"{list_candidate[0]} with {(c_rounded)*100:.3f}%, \n"
      f"{list_candidate[1]} with {(d_rounded)*100:.3f}%, \n"
      f"{list_candidate[2]} with {(r_rounded)*100:.3f}%\n")
    txto.write(f'Winner is {list_candidate[1]}')




