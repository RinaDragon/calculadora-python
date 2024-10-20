import pandas as pd  # Para manejar los datos
import matplotlib.pyplot as plt  # Para la visualización

# Cargar dataset Iris
df = pd.read_csv('iris.csv')

# Mostrar las primeras 5 filas
print(df.head())

# Graficar la longitud del sépalo
df['sepal_length'].plot(kind='hist', bins=20, title='Distribución de la longitud del sépalo')
plt.xlabel('Longitud del sépalo')
plt.ylabel('Frecuencia')
plt.show()
