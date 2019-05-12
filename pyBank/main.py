import os
import csv
# specifying the files path directories
Revenue_path = os.path.join("..","Resources", "budget_data.csv")
output_path = os.path.join("..","Resources", "Financial_report.txt")
# declaring parameters for counting
Net_total = 0
Total_number_months = 0
Change_list = []
months_list = []
            
with open(Revenue_path, newline='') as budget_file:
    Budget = csv.reader(budget_file, delimiter=',')
    next(Budget)
    Total_number_months = Total_number_months + 1
    first_row = next(Budget)
    Net_total = Net_total + int(first_row[1])
    prev_net = int(first_row[1])
 # calculate changes in profit/loss   
    for row in Budget:
        Net_total= Net_total + int(row[1])
        Total_number_months+=1
        change = int(row[1]) - prev_net
        Change_list.append(change)
        months_list.append(row[0])
        prev_net = int(row[1])
# calculting the Average changes
Average = sum(Change_list) / len(Change_list)
greatest_increase = max(Change_list)
greatest_decrease = min(Change_list)
for change in Change_list:
    if change == int(greatest_increase):
        greatest_increase_value = change
        greatest_increase_month = months_list[Change_list.index(change)]
        pass
    if change == int(greatest_decrease):
        greatest_decrease_value = change
        greatest_decrease_month = months_list[Change_list.index(change)]
        pass

output = (f"\n Finacial Analysis \n"
f"----------------------------------------\n"
f"the total number of months is {Total_number_months}\n"
f"the net toatl is {Net_total}\n"
f"Average change :  {Average}\n"
f"greatest increase in profit: {greatest_increase_month} |({greatest_increase_value})\n"
f"greatest increase in profit: {greatest_decrease_month} | ({greatest_decrease_value})\n")

print(output)

#tranfer the results to text file
with open(output_path, 'w') as Budget_file:
    Budget_file.write(output)
        