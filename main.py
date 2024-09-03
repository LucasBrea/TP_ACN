import pandas as pd
from matplotlib import pyplot as plt
import math

df = pd.read_excel("TP1 Wind Data.xlsx")

n_row = df.shape[0]

print(df.head())

# df.plot(x="dia", y="regional wind", kind="line")
#
# plt.show()

def theta(i):
    return 6 + 2*math.cos(i*math.pi*2/360)

wind_std =  df.std()

#Calculo el promedio de 'regional wind' y el promedio de 'regional wind'**2 para estimar
#media, varianza y desvio.
mean_wind = 0
mean_wind_sq = 0
for index, row in df.iterrows():
    mean_wind += row['regional wind']
    mean_wind_sq += row['regional wind']**2

mean_wind /= n_row #promedio 'regional wind'
mean_wind_sq /= n_row
print(mean_wind)
print(mean_wind_sq)

sigma_wind = math.sqrt(mean_wind_sq - mean_wind ** 2) #Desvio estimado
print(df['regional wind'].std()) #Desvio real
print(sigma_wind)


#Error estimado del desvio
error_desvio =  1.96*(sigma_wind/math.sqrt(n_row))

print(error_desvio)

#Estructura para loopear los caminos (mean reverting process en las slides)
T = 365 #Daily for a year

delta =  1/T

paths = {}

n_paths =  100

for i in range(n_paths):
    paths[i] = []