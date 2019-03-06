import os
import csv

budget_data = os.path.join(".", "resources", "budget_data.csv")

TotalMonths = 1
TotalNetAmount = 0
TotalChange = 0
profit = 0
loss = 0


# with open(udemy_csv, newline="", encoding='utf-8') as csvfile:
with open(budget_data, newline="") as Budget_data_file:
    csvReader = csv.reader(budget_data, delimiter=",")
    csvHeader = next(csvReader)
    csvRowPrev = next(csvReader)
   
    TotalNetAmount = csvRowPrev
    
    for row in csvReader:

        # Total number of months
        TotalMonths = TotalMonths + 1
        TotalNetAmount = int(row[1]) + TotalNetAmount
        MonthlyChange = int(row[1]) - int(RowPrev[1])
        TotalChange = MonthlyChange + TotalChange

        if MonthlyChange > 0:
            if MonthlyChange > profit:
                profit = MonthlyChange
                profitMonth = row[0]
        elif MonthlyChange < 0:
            if abs(MonthlyChange) > abs(loss):
                loss = MonthlyChange
                lossMonth = row[0]
        
        RowPrev=row
        AverageChange = TotalChange/(TotalMonths - 1)


    print("Financial Analysis")
    print("-------------------")
    print(f"Total Months: {TotalMonths}")
    print(f"Total : {TotalNetAmount}")
    print(f"Average Change: {AverageChange}")
    print(f"Greatest Increase in Profits: {profitMonth} ({profit})")
    print(f"Greatest Increase in Profits: {lossMonth} ({loss})")