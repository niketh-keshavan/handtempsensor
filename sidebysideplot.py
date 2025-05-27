import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

files = [
    'data\FTEMPS_trimmed.CSV',
    #'data\Calmthermistor.csv'
]

fig, ax1 = plt.subplots()
df1 = pd.read_csv(files[0])
t1 = df1['time_s'] / 60
ax1.plot(t1, df1['object_resistance_R'], 'g-', label='thermistor')
ax1.set_xlabel('Time (min)')
ax1.set_ylabel('Ohms', color='g')
ax1.tick_params(axis='y')

"""ax2 = ax1.twinx()
df2 = pd.read_csv(files[1])
t2 = df2['Time (s)'] / 60
ax2.plot(t2, df2['Temperature (F)'], 'b', label = 'calmwand')
ax2.set_xlabel('Time (min)')
ax2.set_ylabel('Temperature', color='b')
ax1.tick_params(axis='y')"""

plt.show()

