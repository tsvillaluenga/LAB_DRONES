import pandas as pd

# Ruta del archivo de Excel
file_path = r'C:\Users\tsvil\Downloads\PLOT\PLOT_MT_T_data_range2.xlsx'

# Leer el archivo de Excel
df = pd.read_excel(file_path, sheet_name=None)

# Nombres de las columnas que queremos mantener
column_names = [
    '/drone0/FollowPathBehavior/_behavior/behavior_status/status',
    '/drone0/GoToBehavior/_behavior/behavior_status/status',
    '/drone0/LandBehavior/_behavior/behavior_status/status',
    '/drone0/TakeoffBehavior/_behavior/behavior_status/status',
    '/resource_monitor/cpu_memory_usage/cpu_usage/percent'
]

# Iterar sobre cada hoja en el archivo de Excel
for sheet in df.keys():
    # Verificar si las columnas de interés existen en la hoja
    if all(col in df[sheet].columns for col in column_names):
        # Mantener solo las columnas de interés
        df[sheet] = df[sheet][column_names]
        # Rellenar las celdas vacías con el valor de la celda anterior de la misma columna
        df[sheet] = df[sheet].fillna(method='ffill')
        
        # Obtener el valor máximo y mínimo de la columna '/resource_monitor/memory_state/total_program_size'
        max_value_E = df[sheet]['/resource_monitor/cpu_memory_usage/cpu_usage/percent'].max()
        min_value_E = df[sheet]['/resource_monitor/cpu_memory_usage/cpu_usage/percent'].min()
        
        # Reemplazar los valores 1 y 0 en las columnas específicas con el valor máximo y mínimo de la columna 'E' respectivamente
        for col in column_names[:-1]:  # Excluir la última columna que es 'E'
            df[sheet][col] = df[sheet][col].apply(lambda x: max_value_E if x == 1 else (min_value_E if x == 0 else x))
    else:
        print(f"La hoja '{sheet}' no contiene todas las columnas seleccionadas. Se omitirá esta hoja.")

# Guardar el archivo de Excel limpio
output_path = r'C:\Users\tsvil\Downloads\PLOT\CPU_5limpio_PLOT_MT_T_data_range2.xlsx'
with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
    for sheet, data in df.items():
        data.to_excel(writer, sheet_name=sheet, index=False)

print(f'Archivo limpio guardado en: {output_path}')
