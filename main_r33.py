import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file from the specified location
file_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0083__Day79_Analyzing_Nobel_Prize_w_Plotly_Matplotlib_Seaborn__240827\NewProject\r00-r09 START\r00_env_START\nobel_prize_data.csv"
df = pd.read_csv(file_path)

# Group by 'birth_country_current' and 'category', and count the total number of prizes won by each country in each category
prizes_by_country_and_category = df.groupby(['birth_country_current', 'category']).size().reset_index(name='total_prizes')

# Filter to only include the top 20 countries by total prizes
total_prizes_by_country = prizes_by_country_and_category.groupby('birth_country_current')['total_prizes'].sum().reset_index()
top20_countries_list = total_prizes_by_country.sort_values(by='total_prizes', ascending=False).head(20)['birth_country_current']
top20_prizes_by_country_and_category = prizes_by_country_and_category[prizes_by_country_and_category['birth_country_current'].isin(top20_countries_list)]

# Set a color palette using Seaborn (hsv)
colors = sns.color_palette('hsv', len(top20_prizes_by_country_and_category['category'].unique()))

# Plot a horizontal bar chart with customized colors, split by categories
plt.figure(figsize=(14, 10))
sns.barplot(
    data=top20_prizes_by_country_and_category,
    y='birth_country_current',
    x='total_prizes',
    hue='category',
    palette=colors,
    dodge=False
)

# Add labels and title
plt.xlabel('Total Number of Prizes Won', fontsize=14)
plt.ylabel('Country', fontsize=14)
plt.title('Top 20 Countries by Total Number of Nobel Prizes Won, Split by Category', fontsize=16)
plt.gca().invert_yaxis()  # Invert y-axis to show the highest values at the top

# Adjust layout to avoid text cutoff
plt.tight_layout(pad=3.0)

# Save the plot as an image file
output_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0083__Day79_Analyzing_Nobel_Prize_w_Plotly_Matplotlib_Seaborn__240827\NewProject\r00-r09 START\r00_env_START\top20_total_prizes_by_country_split_by_category.png"
plt.savefig(output_path)

# No need for plt.show() since we're saving the file
