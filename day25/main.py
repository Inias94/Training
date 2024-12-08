# with open("weather_data.csv", "r") as file:
#     data = file.readlines() # Readlines turns every item in the data to an item in a LIST.
#
# print(data)

import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    print(data)
    # print([row for row in data])
    temperatures = []

    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))

    print(temperatures)
