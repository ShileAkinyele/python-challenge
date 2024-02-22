#importing dependencies
import os
import csv

#storing the file path associated with the csv file
election_csv = os.path.join("Resources", "election_data.csv")

 

#Opening and reading csv
with open(election_csv) as csv_file:
    data = csv.reader(csv_file, delimiter=",")
    
    
#Reading the header row
    csv_header = next(data)
    print(f"Header: {csv_header}")



    num_votes = 0
    candidates=[]
    candidate_votes={}


#getting total votes
    for row in data:
        num_votes+=1

#getting the candidate list  
        candidate=row[2]
        candidates.append(candidate)
        candidates=list(set(candidates))
        print(candidates)
     
#getting the number of votes and percentage votes
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
             candidate_votes[candidate] = 1
    for candidate in candidate_votes:
   

 #number of votes for each candidate
        votes=candidate_votes[candidate]
        print(f"{candidate}: {votes}")
        
 #percentage vote for each candidate
        percentage_vote= (votes/num_votes)*100
        print(f"{candidate}:{percentage_vote:.3f}%")


#specifying the file to write to
output_path = os.path.join( "Analysis", "new.txt")

#writing results into the text file 
with open(output_path, 'w') as datafile:
    datafile.write("Financial Analysis\n")
    datafile.write("---------------------\n")
    datafile.write(f"Total Votes: {num_votes}\n")




