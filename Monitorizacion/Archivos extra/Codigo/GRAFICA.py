import pandas as pd
import matplotlib.pyplot as plt

# Rutas de los archivos de Excel
file_paths = [
    r'C:\Users\tsvil\Downloads\PLOT\limpio_PLOT_MT_T_data_range2.xlsx',
    r'C:\Users\tsvil\Downloads\PLOT\limpio_PLOT_MT_F_data_range2.xlsx',
    r'C:\Users\tsvil\Downloads\PLOT\limpio_PLOT_ISOLATED_T_data_range2.xlsx',
    r'C:\Users\tsvil\Downloads\PLOT\limpio_PLOT_ISOLATED_F_data_range2.xlsx'
]

# Nombres para la leyenda
labels = ['MT_T', 'MT_F', 'ISOLATED_T', 'ISOLATED_F']

# Diccionario para almacenar los datos de cada archivo
data = {}

# Función para detectar los puntos donde y empieza a aumentar (rising edge)
def detect_rising_edges(y, threshold=0.5):
    rising_edges = []
    for i in range(1, len(y)):
        if y[i] > y[i - 1] + threshold:
            rising_edges.append(i)
    return rising_edges


# Leer cada archivo de Excel y alinear los pulsos
for i, file_path in enumerate(file_paths):
    df = pd.read_excel(file_path)
    # Asumiendo que las columnas de interés son la primera y la segunda
    x_col = df.columns[0]
    y_col = df.columns[1]
    
    x = df[x_col]
    y = df[y_col]
    
    # Detectar subidas (rising edges)
    rising_edges = detect_rising_edges(y)
    
    if len(rising_edges) < 3:
        print(f"Advertencia: No se detectaron al menos 3 subidas en {labels[i]}. Se encontraron {len(rising_edges)} subidas.")
    
    # Normalizar para que el primer pico empiece en x=0
    if rising_edges:
        x_normalized = x - x[rising_edges[0]]
        data[labels[i]] = (x_normalized, y)
    
        # Ajustar los otros pulsos
        for edge in rising_edges[1:]:
            delta_x = x[edge] - x_normalized[rising_edges[0]]
            x_normalized = x_normalized - delta_x

# Crear la gráfica
plt.figure(figsize=(10, 6))

for label, (x, y) in data.items():
    plt.plot(x, y, label=label)

plt.xlabel('Tiempo')
plt.ylabel('Total Program Size (bytes)')
plt.title('Comparación de Datos Composable Distintos Contenedores')
plt.legend()
plt.grid(True)
plt.show()
