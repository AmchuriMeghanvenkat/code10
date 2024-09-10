# with open("weather_data (1).csv") as data_file:
#     data=data_file.readlines()
#     print(data)
# import csv
#
# with open("weather_data (1).csv") as data_file:
#     data=csv.reader(data_file)
#     temperature=[]
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)
import pandas

data=pandas.read_csv("weather_data (1).csv")
# temp_list=data["temp"].to_list()
# print(temp_list)
# average=sum(temp_list)/len(temp_list)
# print(average)
print(data[data.temp==12])
