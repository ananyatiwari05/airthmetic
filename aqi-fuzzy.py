import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import skfuzzy as fuzz
from skfuzzy import control as ctrl

df = pd.read_csv('city_day.csv')
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df = df[(df['City'] == 'Delhi') & (df['Year'] == 2019)]
df = df[['PM2.5', 'PM10', 'NO2']].dropna().reset_index(drop=True)

pm25 = ctrl.Antecedent(np.arange(0, 501, 1), 'PM2.5')
pm10 = ctrl.Antecedent(np.arange(0, 501, 1), 'PM10')
no2 = ctrl.Antecedent(np.arange(0, 201, 1), 'NO2')
aqi = ctrl.Consequent(np.arange(0, 11, 1), 'AQI')

pm25.automf(5)
pm10.automf(5)
no2.automf(5)

aqi['excellent'] = fuzz.trimf(aqi.universe, [0, 0, 2])
aqi['good'] = fuzz.trimf(aqi.universe, [1, 3, 5])
aqi['moderate'] = fuzz.trimf(aqi.universe, [3, 5, 7])
aqi['poor'] = fuzz.trimf(aqi.universe, [5, 7, 9])
aqi['hazardous'] = fuzz.trimf(aqi.universe, [8, 10, 10])

rule1 = ctrl.Rule(pm25['good'] & pm10['good'] & no2['good'], aqi['excellent'])
rule2 = ctrl.Rule(pm25['average'] | pm10['average'] | no2['average'], aqi['moderate'])
rule3 = ctrl.Rule(pm25['poor'] | pm10['poor'] | no2['poor'], aqi['poor'])
rule4 = ctrl.Rule(pm25['poor'] & pm10['poor'], aqi['hazardous'])

aqi_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4])

aqi_sim = ctrl.ControlSystemSimulation(aqi_ctrl)

print("Simulated AQI Output (First 10 Days):")
for i in range(10):
    aqi_sim.input['PM2.5'] = df.loc[i, 'PM2.5']
    aqi_sim.input['PM10'] = df.loc[i, 'PM10']
    aqi_sim.input['NO2'] = df.loc[i, 'NO2']
    aqi_sim.compute()
    print(f"Day {i+1}: AQI Score = {aqi_sim.output['AQI']:.2f}")

plt.figure(figsize=(10, 5))
aqi.view()
plt.title("AQI Output Membership Functions", fontsize=14)
plt.tight_layout()
plt.draw()
plt.pause(0.001)

num_days = min(60, len(df))
aqi_scores = []

for i in range(num_days):
    aqi_sim.input['PM2.5'] = df.loc[i, 'PM2.5']
    aqi_sim.input['PM10'] = df.loc[i, 'PM10']
    aqi_sim.input['NO2'] = df.loc[i, 'NO2']
    aqi_sim.compute()
    aqi_scores.append(aqi_sim.output['AQI'])

plt.figure(figsize=(14, 7))

# Plot AQI scores
plt.plot(range(1, num_days + 1), aqi_scores, marker='o', color='mediumblue', linewidth=3)

# Add shaded AQI zones (adjusted for zoomed view)
plt.axhspan(4, 5, facecolor='#d4f4dd', alpha=0.5, label='Excellent')
plt.axhspan(5, 6, facecolor='#b3e5fc', alpha=0.5, label='Good')
plt.axhspan(6, 7, facecolor='#fff9c4', alpha=0.5, label='Moderate')
plt.axhspan(7, 8, facecolor='#ffe0b2', alpha=0.5, label='Poor')

# Set y-axis zoom range
plt.ylim(4, 8)

# Title and labels
plt.title("Fuzzy Air Quality Index Estimation\nDelhi, 2019 (First 60 Days)", fontsize=24, fontweight='bold', pad=20)
plt.xlabel("Day", fontsize=18, labelpad=10)
plt.ylabel("Fuzzy AQI Score", fontsize=18, labelpad=10)

# Axis ticks and layout
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(loc='upper left', fontsize=14, frameon=True)
plt.tight_layout(pad=3.0)
plt.show()
