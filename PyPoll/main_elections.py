#Elections Analysis

import os

import csv

election_csvpath = os.path.join('C:/Users/emanu/repos/HW Challenges/python-challenge (HW3)/PyPoll/resources/election_data.csv')
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

text_output = os.path.join("C:/Users/emanu/repos/HW Challenges/python-challenge (HW3)/PyPoll/analysis/", "election_textfile.txt")
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




