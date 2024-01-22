from flask import Flask, render_template
import plotly.express as px
import json
import os

app = Flask(__name__)

# Check if the JSON file exists
json_file_path = 'all_capitals_data.json'
if os.path.exists(json_file_path):
    # Load the generated data from the JSON file
    with open(json_file_path, 'r') as file:
        data = json.load(file)["Capitals"]
else:
    data = {}

# Create a Plotly figure for each capital and month
figures = []
for capital, months_data in data.items():
    for month, month_data in months_data.items():
        names = month_data["People"].split(", ")
        lengths = list(map(int, month_data["Length"].split(", ")))

        # Create a histogram for name frequency
        name_histogram = px.histogram(x=names, title=f'Name Frequency in {month} for {capital}', labels={'x': 'Names', 'y': 'Frequency'})
        figures.append(name_histogram)

        # Create a histogram for length frequency
        length_histogram = px.histogram(x=lengths, title=f'Length Frequency in {month} for {capital}', labels={'x': 'Length', 'y': 'Frequency'})
        figures.append(length_histogram)

# Define a route to render the dashboard
@app.route('/')
def dashboard():
    return render_template('dashboard.html', figures=figures)

if __name__ == '__main__':
    app.run(debug=True)
