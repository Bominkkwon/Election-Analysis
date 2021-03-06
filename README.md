# Election-Analysis


## Table of Contents
* [Project title](#project-title)
* [Technologies](#technologies)
* [Overview](#overview)
* [Analysis](#analysis)




## Project title
Election Analysis - Module 3 Challenge 

## Technologies
[Python](https://www.python.org/downloads/ "Download Python") 3.7.9.

## Overview 
The dataset, [election_results.csv](https://github.com/Bominkkwon/Election-Analysis/tree/main/Resources "Resources/eletion_results.csv"), that is given for this project consists of a number for the ballot ID and a name for the county and candidate, respectively. In this project, our final Python script will need to be able to deliver the following information when the script is run to complete the audit: 
* Total number of votes cast
* A complete list of candidates who received votes
* Total number of votes each candidate received
* Percentage of votes each candidate won
* The winner of the election based on popular vote
* The voter turnout for each county
* The percentage of votes from each county out of the total count
* The county with the highest turnout

## Analysis
## [Election-Audit Results](https://raw.githubusercontent.com/Bominkkwon/Election-Analysis/main/analysis/election_results.txt)

* How many votes were cast in this congressional election?

```Python
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1
```
        
369,711 votes were cast in this congressional election.
        
* Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
```Python
    for county_name in county_votes:
    #     # Retrieve the county vote count.
        county_votecount = county_votes[county_name]
    #     # Calculate the percentage of votes for the county.
        county_percentage = float(county_votecount) / float(total_votes) * 100
```
Jefferson county had 38,855 votes, which is 10.5% of the total votes that were cast in this congressional election.
Denver county had 306,055 votes, which is 82.8% of the total votes that were cast in this congressional election.
Arapahoe county had 24,801 votes, which is 6.7% of the total votes that were cast in this congressional election.

* Which county had the largest number of votes?

Denver had the largest number of votes (306,055 votes).

* Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
```python
       candidate_name = row[2]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
        
        for candidate_name in candidate_votes:
        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
```
Charles Casper Stockham received 85,213 votes, which is 23.0% of the total votes that were cast in this congressional election.
Diana DeGette received 272,892 votes, which is 73.8% of the total votes that were cast in this congressional election.
Raymon Anthony Doane received 11,606, which is 3.1% of the total votes that were cast in this congressional election.

* Which candidate won the election, what was their vote count, and what was their percentage of the total votes?

Diana DeGette, who received 272,896 votes which is 73.8% of the total votes, won the election.

