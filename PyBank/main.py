# Importing Modules
import os
import csv

#Setting Variable for path to budget_data.csv
budgetdata=os.path.join('python-challenge','PyBank','Resources','budget_data.csv') 

#Reading budget_data.csv file
with open(budgetdata) as csvfile:
    budgetreader=csv.reader(csvfile,delimiter=',')

    #Reading headers
    budgetdata_header=next(budgetreader)

    #Setting up lists for Date and Profit/Loss
    profit_loss=[]
    date=[]
    for row in budgetreader:
        profit_loss.append(int(row[1]))
        date.append(row[0])

    #Counting Total Months
    total_months=len(date)

    #Finding Net Profit/Loss
    net_value=sum(profit_loss)

    #Finding average of changes in Profit/Loss
    previous = profit_loss[0]
    change = []
    for current in profit_loss:
        if current != previous:
            indv_change = current - previous
            change.append(indv_change)
            previous = current

    average_change=sum(change)/(total_months-1) #Subtract 1 from total months to account for # of changes

    #Finding Greatest Increase
    maximum=max(change)
    max_change_date=change.index(maximum)+1 #Add back 1 to reference correct index in date[]

    #Finding Greatest Decrease
    minimum=min(change)
    min_change_date=change.index(minimum)+1 #Add back 1 to reference correct index in date[]
    
#Storing Financial Analysis as list
analysis = [str(f'Finanical Analysis'),
            str(f'\n----------------------------'),
            str(f'\nTotal Months: {total_months}'),
            str(f'\nTotal: ${net_value}'),
            str(f'\nAverage Change: ${round(average_change,2)}'), #looked up round()
            str(f'\nGreatest Increase in Profits: {date[max_change_date]} (${maximum})'),
            str(f'\nGreatest Decrease in Profits: {date[min_change_date]} (${minimum})')
]

#Creating path for new .txt file
financial_analysis = os.path.join('python-challenge','PyBank','analysis','Financial Analysis.txt')

#Generating new .txt file for results
def data_analysis(parameter):
    datafile.writelines(parameter)

with open(financial_analysis, "w") as datafile:
    data_analysis(analysis)