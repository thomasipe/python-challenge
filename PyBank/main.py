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
    pl_list = []
    month_list = []
    for row in csvreader:
        # total number of months
        tot_months = tot_months + 1

        #net amount of Profit/Loss
        net_pl = net_pl + int(row[1])

        # create list for avg of profit/loss
        pl_list.append(int(row[1]))           

        #create the month list
        month_list.append(row[0])
    
    #loop through the list to get the changes from month to month
    pl_change = []
    for i in range(1, len(pl_list)) :
        pl_change.append(pl_list[i] - pl_list[i-1])
        #print(pl_change)

    # now that i have month to month changes in a list
    # add them together and divide by the count to get avg pl
    total_pl_change = 0
    ele = 0
    while(ele < len(pl_change)) :
        total_pl_change = total_pl_change + pl_change[ele]
        ele += 1


avg_change = round(total_pl_change/len(pl_change),2)
max_index = pl_change.index(max(pl_change)) +1
min_index = pl_change.index(min(pl_change)) +1
max_month = month_list[max_index]
min_month = month_list[min_index]
max_change = max(pl_change)
min_change = min(pl_change)

print(" ")
print("Financial Analysis")
print("-------------------------------")
print(f"Total Months: {tot_months}")
print(f"Total: ${net_pl}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: {max_month} (${max_change})")
print(f"Greatest Decrease in Profits: {min_month} (${min_change})")
print(" ")







