import csv
import matplotlib.pyplot as plt
import numpy as np


with open("activity.csv")as text:
    data = csv.DictReader(text)
    row0 = next(data)
    int_dict = {}
    steps_day = 0
    steps_day_list = []
    dates = []
    day = 0
    for key in data:
        current_date = key["date"]
        if key["steps"] != "NA":
            if key["interval"] in int_dict:
                int_dict[key["interval"]].append(int(key["steps"]))
            else:
                int_dict[key["interval"]] = [int(key["steps"])]
        if current_date not in dates:
            if day != 0:
                steps_day_list.append(steps_day)
            dates.append(current_date)
            steps_day = 0
            if key["steps"] != "NA":
                steps_day += int(key["steps"])
            day += 1
        else:
            if key["steps"] != "NA":
                steps_day += int(key["steps"])
    for mins in int_dict:
        int_dict[mins] = sum(int_dict[mins]) / len(int_dict[mins])

    print("5 minutes interval with most steps averaged is:", max(list(int_dict.values())))

plt.plot(list(int_dict.keys()), list(int_dict.values()))
plt.xlabel("5 minute interval")
plt.ylabel("Steps per day")
plt.xticks(np.arange(0, max(list(int_dict.values())) + 100, 60))

plt.show()

