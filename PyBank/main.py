import os
import csv

file_path = os.path.join(".","Resources", "budget_data.csv")
# print(file_path)

with open(file_path, "r") as csv_file:
  csv_reader_obj = csv.reader(csv_file, delimiter=",")
  # print(list(csv_reader_obj))
  
  # Read the header row first and move the pointer to next line
  csv_header = next(csv_file)
  print(csv_header)

  data_list = list(csv_reader_obj)
  total_month = len(data_list)
  print(total_month)

  
  total_profit_loss = int(data_list[0][1])
  total_change = 0
  greatest_profit_increase = 0
  greatest_profit_decrease = 0
  previous_month_profit = int(data_list[0][1])

  for i in range(1, total_month):
    current_month_profit = int(data_list[i][1])
    change = current_month_profit - previous_month_profit
    total_profit_loss += current_month_profit
    total_change += change
    previous_month_profit = current_month_profit
    if greatest_profit_increase < change:
      greatest_profit_increase = change
    if greatest_profit_decrease > current_month_profit:
      greatest_profit_decrease = change
  
  print(total_month)
  print(total_profit_loss)
  print(greatest_profit_decrease)
  print(greatest_profit_increase)
  print(f"{total_change / (total_month - 1)}")
    
