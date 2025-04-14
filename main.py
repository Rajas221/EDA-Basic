import pandas as pd #pandas to handle tabular data

df = pd.read_csv('12-31-2020.csv')
df.head()

#Inspection and cleaning of data
df.info() #Shows structure
df.describe() #Gives stats like min max etc
df.isnull().sum() #Shows null values in each column
 
#Total Cases overtime
import matplotlib.pyplot as plt
global_cases = df.groupby('Last_Update')['Active'].sum() #Group by date and sum total cases and sum adds up cases
plt.plot(figsize=(12,6))
plt.plot(global_cases)
plt.title('Total Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Total Cases')   
plt.grid()
plt.show()

#Compare Countries
countries = ['Belgium', 'India', 'China', 'Mexico', 'Russia']
for country in countries:
    country_data = df[df['Country_Region'] == country]
    plt.plot(country_data['Last_Update'], country_data['Active'], label=country)
plt.title('COVID-19 Cases in Selected Countries')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.legend()
plt.show()

#Scatter Plot
import seaborn as sns

sns.scatterplot(data=df[df['Country_Region'].isin(countries)], x='Recovered', y='Active', hue='Country_Region')
plt.title('Total Death vs Total Cases')
plt.show()