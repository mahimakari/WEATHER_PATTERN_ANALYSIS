import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
df = pd.read_csv("india_weather_103cities_30mar_13apr.csv")

# Show first 5 rows
print(df.head())

# Show column names
print(df.columns)

# -----------------------------
# TEMPERATURE ANALYSIS
# -----------------------------
plt.figure(figsize=(8,5))
plt.plot(df['temperature_c'])
plt.title("Temperature Pattern")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.show()

# -----------------------------
# HUMIDITY ANALYSIS
# -----------------------------
plt.figure(figsize=(8,5))
plt.plot(df['relative_humidity'])
plt.title("Humidity Pattern")
plt.xlabel("Days")
plt.ylabel("Humidity")
plt.show()

# -----------------------------
# PRECIPITATION ANALYSIS
# -----------------------------
plt.figure(figsize=(8,5))
plt.plot(df['precipitation_amount'])
plt.title("Precipitation Pattern")
plt.xlabel("Days")
plt.ylabel("Precipitation")
plt.show()

# -----------------------------
# BASIC INFORMATION
# -----------------------------
print("\nAverage Temperature:")
print(df['temperature_c'].mean())

print("\nMaximum Temperature:")
print(df['temperature_c'].max())

print("\nMinimum Temperature:")
print(df['temperature_c'].min())