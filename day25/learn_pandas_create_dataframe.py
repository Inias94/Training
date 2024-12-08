import pandas

data = pandas.read_csv("weather_data.csv")

data_dict = {
    "students" : ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

self_made_data = pandas.DataFrame(data_dict)
print(self_made_data)

self_made_data.to_csv("self_made.csv")