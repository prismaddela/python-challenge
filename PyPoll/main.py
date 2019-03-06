import os
import csv

ElecDataCSV = os.path.join(".", "Resources", "election_data.csv")

TotalVotes=0
CanditateVotes={}
a = 0


# with open(udemy_csv, newline="", encoding='utf-8') as csvfile:
with open(ElecDataCSV, newline="") as ElecDataCSVfile:
    CsvReader = csv.reader(ElecDataCSVfile, delimiter=",")
    CsvHeader = next(CsvReader)
   
    
    for row in CsvReader:
        TotalVotes = TotalVotes + 1
        if row[2] not in CanditateVotes:
            CanditateVotes[row[2]] = a
        if row[2]  in CanditateVotes:
               CanditateVotes[row[2]] = CanditateVotes.get(row[2]) +1

    
    print("Election Results")
    print("---------------------")
    print(f"Total Votes : {TotalVotes}")
    print("---------------------")
    
    for key in  CanditateVotes:
        print(f" {key}:{(CanditateVotes[key]/TotalVotes) * 100}% ({CanditateVotes[key]})")
