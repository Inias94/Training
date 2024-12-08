import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

sq_colors = data["Primary Fur Color"]
total_of_colors = sq_colors.value_counts()
print(total_of_colors)

total_of_colors.to_csv("squirrel_count")


