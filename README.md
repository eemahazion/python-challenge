# Python-Challenge

In this challenge I utilize python to analyze data of a bank’s monthly profits (PyBank) in a span of a few years.

I also utilize python to analyze election data (PyPoll) from a small rural town, as their process is not modernized.

Both analyses are done by pulling data from a csv file.
We imported the os and csv library from Python, in order to read the csv files containing the raw data. At the conclusion of the analysis, the output was exported to a text file, for readability.

For the PyBank analysis, we use Python script to calculate the following values:
* The total number of months included in the dataset
* The net total amount of "Profit/Losses" over the entire period
* The changes in "Profit/Losses" over the entire period, and then the average of those changes
* The greatest increase in profits (date and amount) over the entire period
* The greatest decrease in profits (date and amount) over the entire period
For the PyPoll analysis, we use Python script to calculate the following values:
* The total number of votes cast
* A complete list of candidates who received votes
* The percentage of votes each candidate won
* The total number of votes each candidate won
* The winner of the election based on popular vote

Results
Our results for PyBank are as follows:
* The total number of months included in the dataset is 86
* The total net income is $22,564,198
* The average change in income was $-8,311.11 daily
* The greatest increase in profits was for the month of Aug-16 in the amount of $1,862,002
* The greatest decrease in profits was for the month of Feb-14 in the amount of $-1,825,558
Our results for PyPoll are as follows:
* The amount of votes casted was 369,711
* Candidates on the ballot were Charles Casper Stockham, Diana DeGette, and Raymon Anthony Doane
* The vote count was as follows: Charles Casper Stockham with 85213, Diana DeGette with 272892, and Raymon Anthony Doane with 11606
* The election results were as follows: Charles Casper Stockham with 23.049%, Diana DeGette with 73.812%, Raymon Anthony Doane with 3.139%
* Winner is Diana DeGette

Conclusion/Final Analysis:
PyBank: The bank averaged a small amount (relatively speaking) when it comes to change in profit, month over month. This is not to be confused with averaging a loss, as that would deem the bank unprofitable. When I look at profit, month over month, they averaged over $260,000 over the 4-year span. With this knowledge I can ask more questions, as this would make me think profits were larger earlier on and gradually fell, but that would take more analysis, outside of the objective. Nonetheless, this would be valuable information to have as more recommendations could be made to the bank executives. If this was a public company, falling profits would be a bad sign, and a course of action would be recommended.

PyPoll: This rural county had a large amount of votes casted for a spread sheet to handle, so we use Python to crunch this data. The candidate Diana won a large majority of votes in this election. Looking at the raw data, we see that we have data for county, and from this we could draw valuable insights if we were doing an analysis on behalf of the candidates on what areas to campaign on, and how they could improve their chances for the future. All of that is outside of the objective, but insightful information. Python was powerful enough to crunch the data of almost half a million rows, including 3 columns, where this would not be ideal to analyze in Microsoft Excel.

