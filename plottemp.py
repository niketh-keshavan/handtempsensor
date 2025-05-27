import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

# Windows 

"""
files = [
    'data/60-Second_Temperature_Data_in_Celsius__Less_Noise_.csv',
    'data/TemperatureData5_26.csv',
    #'data/HandData5_26.csv',
]
"""

# MacOS

files = [
    'handtempsensor/data/60-Second_Temperature_Data_in_Celsius__Less_Noise_.csv',
    'handtempsensor/data/TemperatureData5_26.csv',
    'handtempsensor/data/TEMPS_extended_linear_ultrasmooth_round3.csv',
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
offset_min += df2['Time (s)'].max() / 60

df3 = pd.read_csv(files[2])
t3 = df3['time_s'] / 60 + offset_min
plt.plot(t3, (df3['object_temp_C'] * 9/5 + 32), color = 'gray', alpha = 0.3)
print(df3['object_temp_C'].max())

temps = df3['object_temp_C']
df3['temp_sg'] = savgol_filter(temps, window_length=41, polyorder=2, mode='interp')
#plt.plot(t3, df3['temp_sg'] * 9/5 + 32, label='Savitzky–Golay')

window_size = 11  # must be odd if you center the window
df3['temp_ma'] = df3['object_temp_C'].rolling(window=31, center=True).mean()
plt.plot(t3, df3['temp_ma'] * 9/5 + 32, label='mov avg')

offset_min += df3['time_s'].max() / 60


ax = plt.gca()
ax.set_xlim([0, offset_min])
ax.set_ylim([90, 100])
plt.title('Temperature vs Time')
plt.show()