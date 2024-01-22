import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ipywidgets as widgets
from ipywidgets import interact

# Read CSV file into a DataFrame
df = pd.read_csv('output.csv')

# Function to update plots based on selected county
def update_plots(selected_county):
    plt.clf()  # Clear the previous plots

    # Filter DataFrame based on selected county
    selected_df = df[df['county'] == selected_county]

    # Subplot 1: Bar chart for the number of visits per county
    plt.subplot(1, 3, 1)
    county_visits = selected_df['county'].value_counts()
    county_visits.plot(kind='bar', xlabel='County', ylabel='Number of Visits', title='Number of Visits per County')

    # Subplot 2: Heatmap for the number of visits per county and month
    plt.subplot(1, 3, 2)
    heatmap_data = selected_df.pivot_table(index='county', columns='month', values='vacation_length', aggfunc='count', fill_value=0)
    sns.heatmap(heatmap_data, annot=True, cmap='YlGnBu', fmt='g', cbar_kws={'label': 'Number of Visits'}, linewidths=.5)
    plt.title('Number of Visits per County and Month')

    # Subplot 3: Pie chart for the average vacation length per month
    plt.subplot(1, 3, 3)
    average_vacation_per_month = selected_df.groupby('month')['vacation_length'].mean()
    plt.pie(average_vacation_per_month, labels=average_vacation_per_month.index, autopct='%1.1f%%', startangle=90)
    plt.title('Average Vacation Length per Month')

    # Adjust layout
    plt.tight_layout()
    plt.show()

# Create a dropdown widget with county options
county_dropdown = widgets.Dropdown(
    options=df['county'].unique(),
    value=df['county'].unique()[0],
    description='Select County:',
    style={'description_width': 'initial'}
)

# Use the interact function to update plots based on selected county
interact(update_plots, selected_county=county_dropdown)
