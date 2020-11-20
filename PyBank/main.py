import os
import csv

# Path to collect data from the Resources folder
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #header 
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}") 

    tot_months = 0
    net_pl = 0
    pl = []
    for row in csvreader:
        # total number of months
        tot_months = tot_months + 1

        #net amount of Profit/Loss
        
        net_pl = net_pl + int(row[1])

        #avg of profit/loss
        #print(row[1])           

print(tot_months)
print(net_pl)





