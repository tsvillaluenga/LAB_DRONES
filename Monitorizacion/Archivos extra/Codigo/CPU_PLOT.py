import pandas as pd
import matplotlib.pyplot as plt

# Ruta del archivo de Excel
file_path = r'C:\Users\tsvil\Downloads\PLOT\CPU_5limpio_PLOT_MT_T_data_range2.xlsx'

# Leer el archivo de Excel
df = pd.read_excel(file_path)

# Nombres de las columnas que queremos graficar
column_names = [
    '/drone0/FollowPathBehavior/_behavior/behavior_status/status',
    '/drone0/GoToBehavior/_behavior/behavior_status/status',
    '/drone0/LandBehavior/_behavior/behavior_status/status',
    '/drone0/TakeoffBehavior/_behavior/behavior_status/status',
    '/resource_monitor/cpu_memory_usage/cpu_usage/percent'
]

# Nombres personalizados para la leyenda
legend_names = [
    'Follow Path Behavior',
    'Go To Behavior',
    'Land Behavior',
    'Takeoff Behavior',
    'CPU Usage Percent'
]

# Verificar si las columnas de interés existen en el DataFrame
if all(col in df.columns for col in column_names):
    # Crear la gráfica
    plt.figure(figsize=(10, 6))
    
    # Graficar cada columna con el nombre personalizado en la leyenda
    for col, legend_name in zip(column_names, legend_names):
        plt.plot(df[col], label=legend_name)
    
    # Añadir etiquetas y título
    plt.xlabel('Tiempo')
    plt.ylabel('CPU (%)')
    plt.title('MT_T - CPU Usage Percent')
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.show()
else:
    print("El archivo no contiene todas las columnas seleccionadas.")
