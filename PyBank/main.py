{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Financial Analysis\n",
      "-----------------------\n",
      "Total months: 86\n",
      "Total: 38382578\n",
      "Average Change: 446309.05\n",
      "Greatest Increase in Profits: 1170593\n",
      "Greatest Decrease in Profits: -1196225\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "import csv\n",
    "\n",
    "path_input = os.path.join(\"Resources\", \"budget_data.csv\")\n",
    "path_output = os.path.join(\"Analysis\", \"budget_data_result.csv\")\n",
    "\n",
    "# ---------------------------\n",
    "# Read data from source file\n",
    "with open(path_input, 'r') as csv_input:\n",
    "    \n",
    "    csv_reader = csv.reader(csv_input, delimiter = ',')\n",
    "  \n",
    "    #Skip the headers\n",
    "    next(csv_reader)\n",
    "    \n",
    "    # Add budget data values to the List     \n",
    "    profit_column = [int(row[1]) for row in csv_reader]\n",
    "    \n",
    "    # Calculate the total number of months included in the dataset\n",
    "    number_of_months = len(profit_column)\n",
    "    \n",
    "    # Calculate the net total amount of \"Profit/Losses\" over the entire period\n",
    "    total_amount = sum(profit_column)\n",
    "    \n",
    "    # Calculate the average of the changes in \"Profit/Losses\" over the entire period\n",
    "    average = round(total_amount/number_of_months,2)\n",
    "    \n",
    "    # Calculate the greatest increase in profits (date and amount) over the entire period\n",
    "    great_increase = max(profit_column)\n",
    "    \n",
    "    # Calculate the greatest decrease in losses (date and amount) over the entire period\n",
    "    great_decrease = min(profit_column)\n",
    "    \n",
    "    header_list = [\"Total months\", \"Total\", \"Average Change\", \n",
    "                   \"Greatest Increase in Profits\", \"Greatest Decrease in Profits\"]\n",
    "    \n",
    "    value_list = [number_of_months, total_amount, average, great_increase, great_decrease] \n",
    "    \n",
    "    result_tuple = zip(header_list, value_list)\n",
    "    \n",
    "    print(\"\\nFinancial Analysis\\n-----------------------\")\n",
    "\n",
    "    for i in range(0,len(header_list)):\n",
    "        print(f\"{header_list[i]}: {value_list[i]}\")\n",
    "        \n",
    "# ---------------------------------------------------------\n",
    "# Write result to the output file\n",
    "with open(path_output, 'w') as csv_output:\n",
    "    \n",
    "    csv_writer = csv.writer(csv_output, delimiter = ',')\n",
    "    \n",
    "    csv_writer.writerow([\"\\nFinancial Analysis\\n---------------------\"])\n",
    "    \n",
    "    for my_tuple in result_tuple:\n",
    "        csv_writer.writerow(my_tuple)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
