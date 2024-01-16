import pandas as pd

file_path = ('C:\\Users\\admin\\Desktop\\programming\\NCHS.csv')
data = pd.read_csv(file_path)

simplified_data = data.drop(columns=['113 Cause Name'])

simplified_summary = simplified_data.groupby('Cause Name').agg(
    Total_Deaths=pd.NamedAgg(column='Deaths', aggfunc='sum'),
    Average_Age_Adjusted_Death_Rate=pd.NamedAgg(column='Age-adjusted Death Rate', aggfunc='mean')
).reset_index()

simplified_summary.head()

top_cases_summary =simplified_summary.sort_values(by='Total_Deaths', ascending=False).head(10)

top_cases_summary.reset_index(drop=True, inplace=True)
print(top_cases_summary)