import pandas as pd

# Load the CSV file
data= pd.read_csv('C:\\Users\\admin\\Desktop\\programming\\NCHS.csv')

#Simplify the dataset by removing the detailed cause of death column and retaining a more general cause of death
simplified_data = data.drop(columns=['113 Cause Name'])

# Aggregate data, providing a summary of each cause of death for all years and states
# Summing the total number of deaths for each cause and calculating the average age-adjusted death rate
simplified_summary = simplified_data.groupby('Cause Name').agg(
    Total_Deaths=pd.NamedAgg(column='Deaths', aggfunc='sum'),
    Average_Age_Adjusted_Death_Rate=pd.NamedAgg(column='Age-adjusted Death Rate', aggfunc='mean')
).reset_index()

simplified_summary.head()

# Showing the first few lines of the simplified summary
# Simplify the data further by limiting the summary to the top causes of death based on the total number of deaths.
# Sort the data by total number of deaths and select the most predominant cause of deaths
top_cases_summary =simplified_summary.sort_values(by='Total_Deaths', ascending=False).head(10)
top_cases_summary.reset_index(drop=True, inplace=True)
print(top_cases_summary)

import matplotlib.pyplot as plt
import seaborn as sns

# Filtering data sets
causewise_trends = data[data['State'] == 'United States'].pivot(index='Year', columns='Cause Name', values='Deaths')

# Setting Up the Plot
plt.figure(figsize=(15, 8))

# Creating the Line Plot
sns.lineplot(data=causewise_trends)

# Adding drawing titles and labels
plt.title("Trends in Deaths by Cause Over Years in United States")
plt.xlabel("Year")
plt.ylabel("Number of Deaths")
plt.xticks(rotation=45)

# Setup Legend
plt.legend(title='Cause of Death', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# Filter data for specified years and regions
year=2017
comparison_data = data[data['Year'] == year]
comparison_data = comparison_data[comparison_data['State'] == 'United States']

# Initialising the drawing
plt.figure(figsize=(10, 6))

# Creating Bar Charts
sns.barplot(x='Deaths', y='Cause Name', data=comparison_data, palette='deep')

# Adding plot titles and axis labels
plt.title(f"Comparison of Causes of Death in {year}")
plt.xlabel("Number of Deaths")
plt.ylabel("Cause of Death")
plt.tight_layout()
plt.show()

# Initialising the drawing
rate_data = data[data['Year'] == year]

# Creating Bar Charts
plt.figure(figsize=(10, 6))

# Adding plot titles and axis labels
sns.barplot(x='Age-adjusted Death Rate', y='Cause Name', data=rate_data, palette='coolwarm')
plt.title(f"Age-adjusted Death Rates by Cause in {year}")
plt.xlabel("Age-adjusted Death Rate")
plt.ylabel("Cause of Death")
plt.tight_layout()
plt.show()

import numpy as np

# Plotting a bar graph showing the top three causes of death each year
# Identify the top three causes of death each year
top_causes_each_year = simplified_data .groupby('Year').apply(lambda x: x.nlargest(3, 'Deaths')).reset_index(drop=True)

# Pivot this data to make it suitable for bar charting
pivot_data_bar = top_causes_each_year.pivot(index='Year', columns='Cause Name', values='Deaths').fillna(0)

# Plotting
pivot_data_bar.plot(kind='bar', stacked=True, figsize=(15, 8), colormap='viridis')
plt.title('Top Three Causes of Death Each Year')
plt.xlabel('Year')
plt.ylabel('Number of Deaths')
plt.legend(title='Cause of Death', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

# Filtering data for a specific cause of death
# Select "Heart Disease" for demonstration
cause_of_death = "Heart disease"
filtered_data = data[data['Cause Name'] == cause_of_death]

# Pivot on data, with years as columns and states as rows
pivot_data = filtered_data.pivot(index='State', columns='Year', values='Deaths')

# Remove the "United States" line and focus on individual states
pivot_data = pivot_data.drop('United States', axis=0)

# Creating Line Charts
plt.figure(figsize=(15, 8))
sns.lineplot(data=pivot_data.T, dashes=False, palette='tab10', linewidth=1.5)
plt.title(f"Deaths Due to {cause_of_death} Over the Years by State")
plt.xlabel("Year")
plt.ylabel("Number of Deaths")
plt.xticks(rotation=45)
plt.legend(title='State', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()