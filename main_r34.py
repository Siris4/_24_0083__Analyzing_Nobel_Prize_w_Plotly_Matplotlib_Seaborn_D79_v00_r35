import pandas as pd

# Load the CSV file from the specified location
file_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0083__Day79_Analyzing_Nobel_Prize_w_Plotly_Matplotlib_Seaborn__240827\NewProject\r00-r09 START\r00_env_START\nobel_prize_data.csv"
df = pd.read_csv(file_path)

# Group by 'birth_country_current' and 'year', and count the number of prizes won by each country in each year
prizes_by_country_and_year = df.groupby(['birth_country_current', 'year']).size().reset_index(name='annual_prizes')

# Sort the DataFrame by 'birth_country_current' and 'year'
prizes_by_country_and_year = prizes_by_country_and_year.sort_values(by=['birth_country_current', 'year'])

# Calculate the cumulative number of prizes won by each country over the years
prizes_by_country_and_year['cumulative_prizes'] = prizes_by_country_and_year.groupby('birth_country_current')['annual_prizes'].cumsum()

# Display the full resulting DataFrame
pd.set_option('display.max_rows', None)  # Show all rows
print(prizes_by_country_and_year)
