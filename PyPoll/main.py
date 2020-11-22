import os
import csv
import sys

# Path to collect data from the Resources folder
csvpath = os.path.join('Resources', 'election_data.csv')


# Lists to store data
candidates = []
d = {}
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #header 
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}") 

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

# Print the results
winner = max(d, key=d.get)
dl = "--------------------------"
tv = (str(tot_votes))

print(" ")
print("Election Results")
print(dl)
print(f"Total Votes: {tv}")
print(dl)

for k, v in d.items() :
    pv = v/tot_votes *100
    pct_of_vote = str(round(pv,3))
    print(str(k)+': '+ pct_of_vote + '% ('+str(v)+')')
print(dl)
print(f"Winner: {winner}")
print(dl)
print(" ")

# save the results out to a file in the Analysis directory

# Now print out the report to the analysis folder
output_file = os.path.join('analysis', 'election_results_rpt.txt')
sys.stdout = open(output_file, "w")
print(" ")
print("Election Results")
print(dl)
print(f"Total Votes: {tv}")
print(dl)

for k, v in d.items() :
    pv = v/tot_votes *100
    pct_of_vote = str(round(pv,3))
    print(str(k)+': '+ pct_of_vote + '% ('+str(v)+')')
print(dl)
print(f"Winner: {winner}")
print(dl)
print(" ")

sys.stdout.close()
