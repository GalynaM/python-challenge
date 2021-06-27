{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Date', 'Profit/Losses']\n",
      "[867884, 984655, 322013, -69417, 310503, 522857, 1033096, 604885, -216386, 477532, 893810, -80353, 779806, -335203, 697845, 793163, 485070, 584122, 62729, 668179, 899906, 834719, 132003, 309978, -755566, 1170593, 252788, 1151518, 817256, 570757, 506702, -1022534, 475062, 779976, 144175, 542494, 359333, 321469, 67780, 471435, 565603, 872480, 789480, 999942, -1196225, 268997, -687986, 1150461, 682458, 617856, 824098, 581943, 132864, 448062, 689161, 800701, 1166643, 947333, 578668, 988505, 1139715, 1029471, 687533, -524626, 158620, 87795, 423389, 840723, 568529, 332067, 989499, 778237, 650000, -1100387, -174946, 757143, 445709, 712961, -1163797, 569899, 768450, 102685, 795914, 60988, 138230, 671099]\n",
      "86\n",
      "38382578\n",
      "446309.05\n",
      "1170593\n",
      "-1196225\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "import csv\n",
    "\n",
    "path = os.path.join(\"Resources\", \"budget_data.csv\")\n",
    "\n",
    "with open(path, 'r') as csv_file:\n",
    "    csv_reader = csv.reader(csv_file, delimiter = ',')\n",
    "  \n",
    "    headers = next(csv_reader)\n",
    "    print(headers)\n",
    "    \n",
    "    profit_column = [int(row[1]) for row in csv_reader]\n",
    "    print(profit_column)\n",
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
    "\n",
    "    print(number_of_months)    \n",
    "    print(total_amount)\n",
    "    print(average)\n",
    "    print(great_increase)\n",
    "    print(great_decrease)\n"
   ]
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
