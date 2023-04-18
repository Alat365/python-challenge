# Importing Modules
import os
import csv

#Setting Variable for path to election_data.csv
electiondata=os.path.join('Resources','election_data.csv')


#Reading election_data.csv file
with open(electiondata) as csvfile:
    electionreader=csv.reader(csvfile,delimiter=',')

    #Reading headers
    electiondata_header=next(electionreader)

    #Setting up lists for Total Votes/Votes per Candidate
    votes=[]
    candidates=[]
    for row in electionreader:
        votes.append(row[0])
        candidates.append(row[2])

    #Finding Individual Candidates 
    indiv_candidates = list(dict.fromkeys(candidates))

    #Counting Total Votes
    total_votes=len(votes)

    #Counting Votes won per Candidate
    candidate1=candidates.count(indiv_candidates[0])
    candidate2=candidates.count(indiv_candidates[1])
    candidate3=candidates.count(indiv_candidates[2])

    count_per_candidate = [candidate1,candidate2,candidate3]

    #Finding percent of votes per candidate
    percent_c1="{0:.3%}".format(candidate1/total_votes)
    percent_c2="{0:.3%}".format(candidate2/total_votes)
    percent_c3="{0:.3%}".format(candidate3/total_votes)

    #Determining Winner
    vote_count = {indiv_candidates[0]:candidate1,indiv_candidates[1]:candidate2,indiv_candidates[2]:candidate3}
    
    winner = max(vote_count, key=vote_count.get)


#Storing Election Results as list
results = [str(f'Election Results'),
            str(f'\n----------------------------'),
            str(f'\nTotal Votes: {total_votes}'),
            str(f'\n----------------------------'),
            str(f'\n{indiv_candidates[0]}: {percent_c1} ({candidate1})'),
            str(f'\n{indiv_candidates[1]}: {percent_c2} ({candidate2})'),
            str(f'\n{indiv_candidates[2]}: {percent_c3} ({candidate3})'),
            str(f'\n----------------------------'),
            str(f'\nWinner: {winner}'),
            str(f'\n----------------------------')
]

#Printing Results in terminal
print(*results)

#Creating path for new .txt file
election_results = os.path.join('analysis','Election Results.txt')

#Generating new .txt file for results
def data_analysis(parameter):
    datafile.writelines(parameter)

with open(election_results, "w") as datafile:
    data_analysis(results)