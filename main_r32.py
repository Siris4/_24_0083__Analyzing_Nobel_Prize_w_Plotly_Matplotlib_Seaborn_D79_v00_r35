import pandas as pd
import plotly.express as px

# Load the CSV file from the specified location
file_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0083__Day79_Analyzing_Nobel_Prize_w_Plotly_Matplotlib_Seaborn__240827\NewProject\r00-r09 START\r00_env_START\nobel_prize_data.csv"
df = pd.read_csv(file_path)

# Group by 'birth_country_current' and count the total number of prizes won by each country
total_prizes_by_country = df.groupby('birth_country_current').size().reset_index(name='total_prizes')

# Sort by the total number of prizes won in descending order and select the top 20 countries
top20_countries = total_prizes_by_country.sort_values(by='total_prizes', ascending=False).head(20)

# Create a choropleth map using Plotly Express with the "Matter" color scale
fig = px.choropleth(
    top20_countries,
    locations="birth_country_current",
    locationmode="country names",
    color="total_prizes",
    hover_name="birth_country_current",
    color_continuous_scale=px.colors.sequential.matter,  # Apply the "Matter" color scale
    labels={"total_prizes": "Total Prizes"},
    title="Top 20 Countries by Total Number of Nobel Prizes Won"
)

# Update layout for better appearance
fig.update_layout(
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular'
    )
)

# Show the figure
fig.show()
