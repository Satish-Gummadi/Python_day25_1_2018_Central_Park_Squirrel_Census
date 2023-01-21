# we can use open to read the file as below
# with open('weather_data.csv') as file:
#     data = file.readlines()
#     print(data)

# but we get data which is difficult to operate in this format
# hence we can use reader method from a library called csv to work with .csv files
# import csv
#
# with open('weather_data.csv') as file_data:
#     data = csv.reader(file_data)
#     temperatures = []
#     for row in data:
#         if row[1].isdigit():
#             temperatures.append(int(row[1]))
#     print(temperatures)

# still, we have written a lot of code just for retrieving a single column
# now this could be done much simpler using pandas library

# import pandas
#
# data = pandas.read_csv('weather_data.csv')
# print(data)
# print(data['temp'])

# not only did it arranged the data into a tabular format and indexed it,
# but also it identified the first row as column names. All it took is 3 lines of code

# # using pandas
# import pandas as pd
#
# data = pd.read_csv('weather_data.csv')
#
# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data['temp'].to_list()
# average = round(sum(temp_list)/(len(temp_list)),2)
# print(average)
# # or
# # we can use mean() method on Pandas Series
# print(data['temp'].mean())
#
# # calculating max value in temp using series
# print(data['temp'].max())
#
# # retrieving a column
# print(data['condition'])    # or
# print(data.condition)
# # in second case the python has already identified the first row column names as attributes,
# # so we can either call it in square brackets or as an attribute
#
# # retrieving an entire row from a DataFrame
# print(data[data['day'] == 'Monday'])
# print(data[data.temp == data.temp.max()])
#
# # retrieving a single element from a particular row
# monday = data[data.day == 'Monday']
# print(monday.condition)
#
# # converting temp of monday into fahrenheit from degree celsius
# monday = data[data.day == 'Monday']
# monday_temp = monday.temp
# monday_temp_faren = (monday_temp * (9/5)) + 32
# print(monday_temp_faren)
#
# # creating pandas DataFrame from scratch
# data_dict = {
#     'Students':
#         ['Satish','Shashank','Sowmya'],
#     'Marks':
#         [70,80,90]
# }
#
# data = pd.DataFrame(data_dict)
# data.to_csv('new_data.csv')

# squirrel census data set

import pandas as pd

data = pd.read_csv('2018_Central_Park_Squirrel_Census.csv')

# print(data.head())

# print(data.columns)
# print(data['Primary Fur Color'].unique())

gray_squirrel_count = data[data['Primary Fur Color'] == 'Gray']['Primary Fur Color'].count()
cinnamon_squirrel_count = data[data['Primary Fur Color'] == 'Cinnamon']['Primary Fur Color'].count()
black_squirrel_count = data[data['Primary Fur Color'] == 'Black']['Primary Fur Color'].count()

print(gray_squirrel_count, cinnamon_squirrel_count, black_squirrel_count)

# creating a dictionary

squirrel_color_dict = {
    'color' : ['Gray','Cinnamon','Black'],
    'count' : [gray_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]
}

# converting a dictionary into dataframe

squirrel_color_df = pd.DataFrame(squirrel_color_dict)

# converting a df to csv file

squirrel_color_df.to_csv('squirrel_color.csv')




