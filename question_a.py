import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
data = pd.read_csv('Facebook.csv', delimiter='\t', usecols=range(3))

# Extract the relevant columns
maus = data['MAU']
total_assets = data['Total Assets']
year = data['Year']

# Create a scatter plot of total assets against MAUs, colored by year
plt.scatter(maus, total_assets, c=year, cmap='plasma')
plt.xlabel('Monthly Active Users (MAUs)')
plt.ylabel('Total Assets')
plt.title('Meta Platforms: Total Assets vs MAUs')
plt.colorbar(label='Year')
plt.show()
