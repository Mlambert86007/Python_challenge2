#Your task is to create a Python script that analyzes the records to calculate each of the following:
#The total number of months included in the dataset
#* The net total amount of "Profit/Losses" over the entire period
#* The changes in "Profit/Losses" over the entire period, and then the average of those changes
#* The greatest increase in profits (date and amount) over the entire period
#* The greatest decrease in profits (date and amount) over the entire period
#Your analysis should look similar to the following:
#  ```text
#  Financial Analysis
 # ----------------------------
  #Total Months: 86
  #Total: $22564198
  #Average Change: $-8311.11
  #Greatest Increase in Profits: Aug-16 ($1862002)
  #Greatest Decrease in Profits: Feb-14 ($-1825558)
  #```
#In addition, your final script should both print the analysis to the terminal and export a text file with the results.

#Begin Task
import os
import csv

#set path for file to read
csvreader = os.path.join('Resources', 'budget_data.csv')

# Assign a variable to save the file to a path.
txtwriter = os.path.join('analysis', 'budget_data.txt')

#Variables to Use

date = []
total_months = []
total_profits = []
profits = 0
total_profts_amount = 0
average_change = 0
profit_increase = []
profit_decrease = []
Gmoney = 0
Lmoney = 0
G_months = 0
L_months = 0
change_average = []
all_dates = []
min_profits = []
max_profits = []
pt02 = 0
gdate = ""
ldate = ""


#Lets Begin This Travesty by reading in the file

with open(csvreader) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #Take out the header
    csvheader = next(csvreader)
   
    #Begin the "For" Loop 
    for row in csvreader:
      
      #Let's Count the Months
      date.append(row[0])
      #all_dates.append(date)

      #Let's Get our the total money (dolla dolla bill y'all) or our losses (bankrupt bankrupt y'all)
      profits = int(row [1])
      total_profits.append(profits)

      pt01 = int(row[1]) - pt02
      pt02 = int(row[1])

      change_average.append(pt01)
   

      if Gmoney < pt01:
          Gmoney = pt01
          gdate = row[0]
          
      if Lmoney > pt01:
          Lmoney = pt01
          ldate = row[0]
change_average[0] = 0          
total_months = len(date)
New_total_profits = sum(total_profits)


#Print Everything
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: ",total_months)
print(f"Total Profits: ${round(New_total_profits, 2)}")
average = sum(change_average)/(len(change_average) -1)
print(f"Average Change: ${round(average, 2)}")
print(f"Greatest increase in profits: ",gdate, f" ${round(Gmoney, 2)}")
print(f"Greatest decrease in profits: ",ldate, f" ${round(Lmoney, 2)}")

#write to text file

financial_analysis1 = (f"Financial Analysis\n" f"----------------------------\n" f"Total Months:  {total_months}\n")
financial_anaylsis2 = (f"Total Profits: ${round(New_total_profits, 2)}\n")
financial_analysis3 = (f"Average Change: ${round(average, 2)}\n")
financial_analysis4 = (f"Greatest increase in profits: {gdate}" f" ${round(Gmoney, 2)}\n")
financial_analysis5 = (f"Greatest decrease in profits: {ldate}" f" ${round(Lmoney, 2)}\n")
                      
with open(txtwriter, "w") as txt_file:
  txt_file.write(financial_analysis1)
  txt_file.write(financial_anaylsis2) 
  txt_file.write(financial_analysis3)
  txt_file.write(financial_analysis4)
  txt_file.write(financial_analysis5)



