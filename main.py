import os
import matplotlib.pyplot as plt
import csv
import pandas as pd
from datetime import datetime
from collections import defaultdict

data = defaultdict(list)  # Dizionario per raggruppare i dati per esercizio
output_dir = "./graph"

# Carica il file CSV
df = pd.read_csv('workouts.csv')
df['start_time'] = pd.to_datetime(df['start_time'], format='%d %b %Y, %H:%M')
df['start_time'] = df['start_time'].dt.strftime('%d/%m/%Y')

# Crea una tabella pivot
pivot_df = df.pivot_table(values='weight_kg',
                          index=['start_time','exercise_title'], 
                          aggfunc='max')

# Salva la tabella pivot in un nuovo CSV
pivot_df.to_csv('data.csv')

# Leggi i dati dal CSV
with open('data.csv', 'r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    next(lines)  # Salta l'intestazione
    for row in lines:
        date = datetime.strptime(row[0], '%d/%m/%Y')  # Converte la data
        exercise = row[1]  # Nome dell'esercizio
        weight = float(row[2])  # Peso
        data[exercise].append((date, weight))  # Raggruppa i dati per esercizio

# Crea un grafico separato per ogni esercizio
for exercise, values in data.items():
    # Ordina i dati per data
    values.sort(key=lambda x: x[0])
    dates = [v[0].strftime('%d/%m/%Y') for v in values]  # Converte le date in stringhe
    weights = [v[1] for v in values]

    # Creazione del grafico
    plt.figure(figsize=(16, 9))
    plt.plot(dates, weights, marker='s', linestyle='solid', label=exercise, color='g')
    for i, weight in enumerate(weights):
        plt.text(dates[i], weight+0.1, f'{weight}', fontsize=10, ha='center', va='bottom')
    plt.gca().set_facecolor('#f0f0f0')
    plt.xticks(rotation=25)
    plt.xlabel('Data')
    plt.ylabel('Peso (kg)')
    plt.title(f'Andamento del Peso - {exercise}', fontsize=20)
    plt.grid()
    plt.legend()

    # Salvataggio come PNG
    filename = os.path.join(output_dir, f'{exercise.replace(" ", "_")}.png')
    plt.savefig(filename, format='png', dpi=500)
    plt.close()  # Chiudi la figura per evitare sovrapposizioni

print("Grafici salvati come PNG!")