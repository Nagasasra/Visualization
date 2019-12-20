import csv
import matplotlib.pyplot as plt
import statistics


with open("activity.csv") as text:
    data = csv.DictReader(text)
    row0 = next(data)
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
        if each_key["steps"] != "NA":
            steps_total += int(each_key["steps"])
            all_steps_list.append(int(each_key["steps"]))
            day_steps_replaced = []
        if current_date_updated not in dates:
            dates.append(current_date_updated)
            if day_iteration != 0:
                stepping_day_60.append(stepping_day)
            stepping_day = 0
            if each_key["steps"] != "NA":
                stepping_day += int(each_key["steps"])
                day_steps_replaced.append(int(each_key["steps"]))
            day_iteration += 1
            number_days_list.append(day_iteration)
        else:
            if each_key["steps"] != "NA":
                if current_date_updated in dates:
                    stepping_day += int(each_key["steps"])
                    day_steps_replaced.append(int(each_key["steps"]))
    stepping_day_60.append(0)
    print("Total Steps:", steps_total)
    print("Total Days:", day_iteration)
    average_steps_per_day = steps_total / day_iteration
    print("The average steps per day is:", average_steps_per_day)
    print("The median of all the steps combined is:", statistics.median(stepping_day_60))

plt.bar(number_days_list, stepping_day_60, 0.50)
plt.xlabel("Day")
plt.ylabel("Steps")
plt.show()
