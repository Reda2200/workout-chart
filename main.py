import os
import matplotlib.pyplot as plt
import csv
import pandas as pd
from datetime import datetime
from collections import defaultdict

data = defaultdict(list)  # Dictionary to group data foreach exercise
output_dir = "./graph" # Output Directory for saving chart

# Load CSV file
df = pd.read_csv('workouts.csv')
df['start_time'] = pd.to_datetime(df['start_time'], format='%d %b %Y, %H:%M')
df['start_time'] = df['start_time'].dt.strftime('%d/%m/%Y')

# Create pivot table
pivot_df = df.pivot_table(values='weight_kg',
                          index=['start_time','exercise_title'], 
                          aggfunc='max')

# Save pivot table in a new CSV file
pivot_df.to_csv('data.csv')

# Read data from pivot table
with open('data.csv', 'r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    next(lines)  # skip header
    for row in lines:
        date = datetime.strptime(row[0], '%d/%m/%Y')  # Convert date
        exercise = row[1]  # Exercise Name
        weight = float(row[2])  # Weight
        data[exercise].append((date, weight))  # Group data foreach exercise

# Create chart foreach exercise
for exercise, values in data.items():
    # Order data by date
    values.sort(key=lambda x: x[0])
    dates = [v[0].strftime('%d/%m/%Y') for v in values]  # Convert Date
    weights = [v[1] for v in values]

    # Chart Creation
    plt.figure(figsize=(16, 9))
    plt.plot(dates, weights, marker='s', linestyle='solid', label=exercise, color='g')
    for i, weight in enumerate(weights):
        plt.text(dates[i], weight+0.1, f'{weight}', fontsize=10, ha='center', va='bottom')
    plt.gca().set_facecolor('#f0f0f0')
    plt.xticks(rotation=25)
    plt.xlabel('Date')
    plt.ylabel('Weight (Kg)')
    plt.title(f'{exercise}', fontsize=20)
    plt.grid()
    plt.legend()

    # Save as .jpg
    filename = os.path.join(output_dir, f'{exercise.replace(" ", "_")}.jpg')
    plt.savefig(filename, format='jpg', dpi=500)
    plt.close()  # Close the figure to avoid overlap

print("Chart saved as JPG!")