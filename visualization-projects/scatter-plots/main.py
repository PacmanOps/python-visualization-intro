# bike sharing dataset hosted at https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset
# follow instructions to import data into python, install repo package
pip install ucimlrepo

# import dataset
from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
bike_sharing = fetch_ucirepo(id=275) 
  
# data (as pandas dataframes) 
X = bike_sharing.data.features 
y = bike_sharing.data.targets 
  
# metadata 
print(bike_sharing.metadata) 
  
# variable information 
print(bike_sharing.variables) 
