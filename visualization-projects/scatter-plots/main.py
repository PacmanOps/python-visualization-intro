# bike sharing dataset hosted at https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset
# follow instructions to import data into python, install repo package https://github.com/uci-ml-repo/ucimlrepo
# hosted files in /data folder for convenience

# import pandas and matplotlib.pyplot
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
bike_sharing = pd.read_csv('data-files/day.csv')

# examine first and last five rows
bike_sharing.head()
bike_sharing.tail()

# examine information about the dataset using .info method
bike_sharing.info()

# convert dteday column from object to datetime
bike_sharing['dteday'] = pd.to_datetime(bike_sharing['dteday'])

# plot line graph, dteday is x-axis and casual is y-axis
# label as Casual
plt.plot(bike_sharing['dteday'], bike_sharing['casual'], label='Casual')

# plot line graph, dteday is x-axis and registered is y-axis
# label as Registered
# on same graph as above
plt.plot(bike_sharing['dteday'], bike_sharing['registered'], label='Registered')

# rotate x-axis ticks 30 degrees
plt.xticks(rotation=30)

# add label bikes rented to y-axis
plt.ylabel("Bikes Rented")

# add label date to x-axis
plt.xlabel("Date")

# Add the title 'Bikes Rented: Casual vs. Registered' 
plt.title('Bikes Rented: Casual vs. Registered')

# Add a legend with 'Casual' and 'Registered' as labels
plt.legend()

# show line graph
plt.show()

# plot line graph with dteday as x-axis and temp as y-axis
plt.plot(bike_sharing['dteday'], bike_sharing['temp'])

# rotate x-axis ticks 45 degrees for readability
plt.xticks(rotation=45)

# show line graph
plt.show()

# create scatter plot, compare windspeed as x-axis and cnt as y-axis
plt.scatter(bike_sharing['windspeed'], bike_sharing['cnt'])

# provide a label for x and y axis and display plot
plt.xlabel('Wind Speed')
plt.ylabel('Bikes Rented')
plt.show()

# show scatter plot, atemp column x-axis and registered y-axis
plt.scatter(bike_sharing['atemp'], bike_sharing['registered'])
plt.show()

# review scatter plot to decide possible correlation
# general positive correlation as increase in atemp/registered correspond
correlation = 'positive'
