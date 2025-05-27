import pandas as pd
import matplotlib.pyplot as plt

files = [
    'data/60-Second_Temperature_Data_in_Celsius__Less_Noise_.csv',
    'data/TemperatureData5_26.csv',
    #'data/HandData5_26.csv',
]

offset_min  = 0
plt.figure()

df1 = pd.read_csv(files[0])
t1 = df1['time_seconds'] / 60
plt.plot(t1, (df1['temperature_C'] * 9/5 + 32))
offset_min += df1['time_seconds'].max() / 60

df2 = pd.read_csv(files[1])
t2 = df2['Time (s)'] / 60 + offset_min - 0.06
plt.plot(t2, (df2['Temperature (F)']))

plt.title('Temperature vs Time')
plt.show()