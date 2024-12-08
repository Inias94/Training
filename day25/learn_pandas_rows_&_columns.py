import pandas

data = pandas.read_csv("weather_data.csv")  # This line is the same as the entire block in the main file.
print(type(data))
print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list, len(temp_list))

# total_temp = 0
# for temp in temp_list:
#     total_temp += temp
print(sum(temp_list) / len(temp_list))

print(data["temp"].mean())

max_temp = data["temp"].max()
# data.temp.max() ## You can use .notation as well (as an attribute)
print(max_temp)

# --- For getting data in a column  above---#

# Get data in Row BELOW
print(data[data.day == "Monday"])

# get the row where the max temperature is present
print(data[data.temp == data.temp.max()])

# Get Mondays temperature and convert to Fahrenheit.
monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
f_temp = monday_temp * 9/5 + 32
print(f"The temp is: {f_temp}")