import os
import csv

# Path to collect data from the Resources folder
csvpath = os.path.join('Resources', 'election_data.csv')


# Lists to store data
candidates = []
d = {}
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #header 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}") 

    tot_votes = 0
    

    for row in csvreader:
        # total number of votes
        tot_votes = tot_votes + 1

        # Add candidate
        candidates.append(row[2])

    for item in candidates :
        if item in d :
            d[item] = d.get(item)+1
        else:
            d[item] = 1

    for k, v in d.items() :
        print(str(k)+':'+str(v))


unique_list = list(set(candidates))
print(unique_list)
print(len(unique_list))
print(tot_votes)
