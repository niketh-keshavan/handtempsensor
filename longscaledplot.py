import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the trimmed CSVs
df1 = pd.read_csv('data/FTEMPS_trimmed.CSV')
df2 = pd.read_csv('data/TemperatureData13_trimmed.csv')

# Identify columns
t1, y1 = 'time_s', 'object_resistance_R'
t2, y2 = 'Time (s)', 'Temperature (F)'

# Compute initial and final values
y1_init = df1[y1].iloc[0]
t_end2 = df2[t2].iloc[-1]
# interpolate y1 at t_end2
y1_end = np.interp(t_end2, df1[t1], df1[y1])

y2_init = df2[y2].iloc[0]
y2_end = df2[y2].iloc[-1]

# Linear scaling factor to align initial and final
alpha = (y1_end - y1_init) / (y2_end - y2_init)

# Apply transformation to df2's y-values
df2['scaled'] = (df2[y2] - y2_init) * alpha + y1_init

# Plot both on the same axes
plt.figure()
plt.plot(df1[t1], df1[y1], label='FTEMPS (resistance)')
plt.plot(df2[t2], df2['scaled'], label='TempData13 (scaled to resistance)')
plt.xlabel('Time (s)')
plt.ylabel('Resistance / Scaled Temperature')
plt.title('Overlay of FTEMPS and TemperatureData13\n(initial & final values aligned)')
plt.legend()
plt.tight_layout()
plt.show()