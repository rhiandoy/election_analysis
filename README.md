# election_analysis

## Resources Used
  - Data: downloaded election_results.csv
  - Software: Python version 3.10, Visual Studio Code, Git Bash

## Overview of Module Project

  For this project, we followed a series of steps using Python, VS Code, and Git Bash to perform an audit on a local election. From a datalist of 369,711 rows, we set out to determine the amount of total votes, the candidates running and how many votes they each received, the perecentage of votes, and the overall winner of the election. 
  
## Project Summary

  In the analysis of this election, it was determined that there were 369,711 votes cast for 3 different candidates.\
  The candidates were:\
        - Charles Casper Stockham\
        - Diana DeGette\
        - Raymon Anthony Doane\
 To determine the results, we found the individual number of votes per candidate as well as the percentage of votes from the total.\
 Charles Stockham received 85,213 votes with 23.0% of the total votes.\
 Diana DeGette finished with 272,892 which was 73.8% of the total votes.\
 Raymon Anthony Doane received 11,606 votes with only 3.1% of the total votes.\
 The winner of this election, by a large margin was Diana Degette with 272,892 votes.
 
 # Election_analysis_Challenge
 
 ## Overview of election audit                  

   After collecting data for the election audit, additional information was 
 needed to determine the voter turnout for each county, the percentage of votes 
 that each county received, and the county with the highest turnout. We began 
 by adding to the PyPoll script created previously which had included similar steps 
 but for candidates instead of counties. To receive information on the counties,
 we created a new list and dictionary to hold the counties and 
 their votes as well as adding an empty string and variable to determine 
 the largest county turnout. The additional script added in this challenge allowed
 us to get more specific with our data. 
    
## Election Audit Results
- In this congressional election, there was a total of 369,711 votes cast out of 3 different counties.
- Arapahoe county had the least amount of votes with 24,801, or 6.7% of the total votes.
- Jefferson county had slightly more with 38,855, 10.5% of the population.
- Denver county had the highest turnout winner with 306,055, or 82.8% of the total votes.
- Each county's vote was retrieved by using the get() function with the variable county_vote.
- To calculate the percentage, I used Cvotes_percentage = float(county_vote) / float(total_votes) * 100
    where Cvotes_percentage was the overall percentage variable and county_vote and total_votes were multiplied by 100 to get a percent. 
![Largest_county_turnout](https://github.com/rhiandoy/election_analysis/blob/64731beb7becdc826f03e645c664a8e658239297/largest_county_turnout.png)
![winning_count](https://github.com/rhiandoy/election_analysis/blob/64731beb7becdc826f03e645c664a8e658239297/winning_count.png)
- The above decision statements were created to hold the winning votes, candidates, percentages, and counties
- To receieve the correct votes and percentages for the candidates, I used the same script written for the counties but modified with different variables. 
- vote_percentage = float(votes) / float(total_votes) * 100
- Out of the 369,711 cast in this election, 23% (85,213) of the votes were given to Charles Casper Stockham.
- 3.1% (11,606) went to the candidate Raymon Anthony Doane.
- 73.8% (272,892) of votes went to Diana DeGette who ultimately won the election.
![election_results](https://github.com/rhiandoy/election_analysis/blob/64731beb7becdc826f03e645c664a8e658239297/Election_results.png)

## Election Audit Summary

 This script can be used and modified for any future or past election if more information was requested. In any voting process, personal details of each individual voter is collected including address, gender, age, nationality, etc. With additional data entered into the csv file, we could modify the script to determine certain age groups and what candidate they voted for. The same could be performed for the other characteristics and demographics.
