import pandas as pd
import matplotlib.pyplot as plt

file_path = 'data\FTEMPS.CSV'

df = pd.read_csv(file_path)
plt.plot(df['time_s'], df['object_temperature_F)'])
plt.show()