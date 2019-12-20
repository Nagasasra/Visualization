import csv
import matplotlib.pyplot as plt
import statistics
import random

with open("activity.csv") as text:
    data_read = csv.reader(text)
    row0 = next(data_read)
    missing = 0
    output = []
    output.append(row0)
    for row in data_read:
        if row[0] == "NA":
            missing += 1
            row[0] = random.randint(0, 100)
        output.append(row)

    print("Total 'NA's:", missing)
    new_file1 = open("activity_mod1.csv", "w")
    writer = csv.writer(new_file1, lineterminator='\n')
    writer.writerows(output)
    new_file1.close()

    new_file2 = open("activity_mod1.csv")
    data = csv.DictReader(new_file2)
    row1 = next(data)
    steps_total = 0
    stepping_day = 0
    stepping_day_60 = []
    day_steps_replaced = []
    all_steps_list = []
    day_iteration = 0
    dates = []
    number_days_list = []
    for each_key in data:
        current_date_updated = each_key["date"]
        steps_total += int(each_key["steps"])
        all_steps_list.append(int(each_key["steps"]))
        day_steps_replaced = []
        if current_date_updated not in dates:
            dates.append(current_date_updated)
            if day_iteration != 0:
                stepping_day_60.append(stepping_day)
            stepping_day = 0
            stepping_day += int(each_key["steps"])
            day_steps_replaced.append(int(each_key["steps"]))
            day_iteration += 1
            number_days_list.append(day_iteration)
        else:
            stepping_day += int(each_key["steps"])
            day_steps_replaced.append(int(each_key["steps"]))
    stepping_day_60.append(0)
    print("Total Steps:", steps_total)
    print("Total Days:", day_iteration)
    average_steps_per_day = steps_total / day_iteration
    print("The average steps per day is:", average_steps_per_day)
    print("The median of all the steps combined is:", statistics.median(stepping_day_60))
    new_file2.close()

plt.bar(number_days_list, stepping_day_60, 0.50)
plt.xlabel("Day")
plt.ylabel("Steps")
plt.show()
