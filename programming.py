import pandas as pd

file_path = ('C:\\Users\\admin\\Desktop\\programming\\NCHS.csv')
data = pd.read_csv(file_path)

simplified_data = data.drop(columns=['113 Cause Name'])

simplified_summary = simplified_data.groupby('Cause Name').agg(
    Total_Deaths=pd.NamedAgg(column='Deaths', aggfunc='sum'),
    Average_Age_Adjusted_Death_Rate=pd.NamedAgg(column='Age-adjusted Death Rate', aggfunc='mean')
).reset_index()
import matplotlib.pyplot as plt
import seaborn as sns
simplified_summary.head()

top_cases_summary =simplified_summary.sort_values(by='Total_Deaths', ascending=False).head(10)

top_cases_summary.reset_index(drop=True, inplace=True)
print(top_cases_summary)
causewise_trends = data[data['State'] == 'United States'].pivot(index='Year', columns='Cause Name', values='Deaths')
plt.figure(figsize=(15, 8))
sns.lineplot(data=causewise_trends)
plt.title("Trends in Deaths by Cause Over Years in United States")
plt.xlabel("Year")
plt.ylabel("Number of Deaths")
plt.xticks(rotation=45)
plt.legend(title='Cause of Death', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()