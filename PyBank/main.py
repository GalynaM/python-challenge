#!/usr/bin/env python
# coding: utf-8

# In[62]:


import os
import csv
import statistics


# In[73]:


path_input = os.path.join("Resources", "budget_data.csv")
path_output = os.path.join("Analysis", "budget_data_result.csv")

# Read data from source file
with open(path_input, 'r') as csv_input: 
    csv_reader = csv.reader(csv_input, delimiter = ',')
   
    # Skip the headers
    next(csv_reader)
    
    # Save data to Dictionary with String Key - Date: Integer Value - Profit/Losses
    date_profit = {}
    for row in csv_reader:
        date_profit[row[0]] = int(row[1])

    #-----------Calculate the total number of months included in the dataset
    number_of_months = len(date_profit)
    
    #-----------Calculate the net total amount of "Profit/Losses" over the entire period
    total_amount = sum(date_profit.values())
    
     
    monthly_change = []
    
    # Get Separate lists for Keys and Values from Dictionary date_profit
    profit_values = list(date_profit.values())
    date_values = list(date_profit.keys())
    
    max_increase=0
    max_decrease=0
    
    for i in range(0, len(date_profit)-1):
         #Calculate the monthly changes in "Profit/Losses" over the entire period
         the_change = list(date_profit.values())[i+1] - list(date_profit.values())[i]
         monthly_change.append(the_change)

         if the_change > max_increase:
            max_increase = the_change
            best_month = list(date_profit.keys())[i+1]

         if the_change < max_decrease:
            max_decrease = the_change
            worst_month = list(date_profit.keys())[i+1]

       

    #-----------Calculate the average of the changes in "Profit/Losses" over the entire period
    average_of_changes = round(statistics.mean(monthly_change), 2)
    
    # Specify variables for the final analysis
    great_increase = (best_month, f"${max_increase}")
    great_decrease = (worst_month, f"${max_decrease}")
  
    
    header_list = ["Total months", "Total", "Average of The Changes",
                   "Greatest Increase in Profits", "Greatest Decrease in Profits"]
    
    value_list = [number_of_months, f"${total_amount}", f"${average_of_changes}",
                  f"{great_increase[0]}: {great_increase[1]}", f"{great_decrease[0]}: {great_decrease[1]}"]

    
    result_tuple = zip(header_list, value_list)
    
    header_row = "\nFinancial Analysis\n-----------------------"
    
    # Analysis output--------------------------------------------------------------------------
    
    #Print result to the terminal
    print(header_row)
    
    for i in range(0,len(header_list)):
        print(f"{header_list[i]}: {value_list[i]}")
   
    # Write result to the output file  
with open(path_output, 'w') as csv_output:
        
    csv_writer = csv.writer(csv_output, delimiter = ',')

    csv_writer.writerow([header_row])

    for my_tuple in result_tuple:
        csv_writer.writerow(my_tuple)


# In[ ]:




