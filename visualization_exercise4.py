import csv
import datetime
import matplotlib.pyplot as plt
import numpy as np

original = open("activity.csv")
data_read = csv.reader(original)
row0 = next(data_read)
if len(row0) == 3:
    row0.append("is_weekdays")
    output = []
    output.append(row0)
    for row in data_read:
        days = row[1].split("-")
        date = datetime.datetime(int(days[0]), int(days[1]), int(days[2]))
        if date.weekday() == 5 or date.weekday() == 6:
            row.append("False")
        else:
            row.append("True")
        output.append(row)
    new_file1 = open("activity_mod2.csv", "w")
    writer = csv.writer(new_file1, lineterminator='\n')
    writer.writerows(output)
    new_file1.close()


new_file2 = open("activity_mod2.csv")
data_read1 = csv.reader(new_file2)
row0 = next(data_read1)
weekend = {}
weekday = {}
for row1 in data_read1:
    if row1[0] != "NA":
        if row1[2] not in weekday:
            weekend[row1[2]] = []
            weekday[row1[2]] = []
        if row1[3] == 'False':
            weekend[row1[2]].append(int(row1[0]))
        else:
            weekday[row1[2]].append(int(row1[0]))
for mins in weekday:
    weekday[mins] = sum(weekday[mins]) / len(weekday[mins])
for mins1 in weekend:
    weekend[mins1] = sum(weekend[mins1]) / len(weekend[mins1])

plt.plot(list(weekday.keys()), list(weekend.values()), list(weekday.values()))
plt.xlabel("5 minute interval")
plt.ylabel("Steps per day")
plt.legend(["Weekend", 'Weekday'])
plt.xticks(np.arange(0, max(list(weekday.values())) + 100, 60))

plt.show()


new_file2.close()

