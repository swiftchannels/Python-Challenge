import os
import csv
# specifying the files path directories
Election_path = os.path.join("..","Resources", "election_data.csv")
output_path = os.path.join("..","Resources", "poll_result.txt")
# decalring the various variables
Total_vote_counts = 0
candidate_list = []
Percentage_list = []
candidate_votes_List = []
candidate_number_votes = 0


# getting the totalnumber of votes and candidates
with open(Election_path, newline='') as Election_file:
        Election_data = csv.reader(Election_file, delimiter=',')
        next(Election_data)
        for row in Election_data:
            Total_vote_counts+= 1
            if row[2] not in candidate_list:
                candidate_list.append(row[2])
# candidate votes and percentage
for candi in candidate_list:
    with open(Election_path, newline='') as Election_file:
        Election_data = csv.reader(Election_file, delimiter=',')
        next(Election_data)
        
        for row in Election_data:
            if row[2] == str(candi):
                candidate_number_votes+= 1
        candidate_votes_List.append(candidate_number_votes)
        Percent = ((candidate_number_votes / Total_vote_counts) * 100)
        Percentage_list.append(Percent)
        candidate_number_votes = 0
#To find the winner of the election
highest_vote = max(candidate_votes_List)
winner = candidate_list[candidate_votes_List.index(highest_vote)]
        
output = (f"\n Total number of votes : {Total_vote_counts} \n"
f"----------------------------------------------------- \n" 
f"{candidate_list[0]} | {Percentage_list[0]}% {candidate_votes_List[0]}\n"    
f"{candidate_list[1]} | {Percentage_list[1]}% {candidate_votes_List[1]}\n"     
f"{candidate_list[2]} | {Percentage_list[2]}% {candidate_votes_List[2]}\n" 
f"{candidate_list[3]} | {Percentage_list[3]}% {candidate_votes_List[3]}\n"      
f" Winner : {winner}\n")   

print(output)

#tranfer the results to text file
with open(output_path, 'w') as Election_file:
    Election_file.write(output)   





