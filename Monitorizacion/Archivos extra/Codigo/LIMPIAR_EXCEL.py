import pandas as pd

# Ruta del archivo de Excel
file_path = r'C:\Users\tsvil\Downloads\PLOT\PLOT_ISOLATED_T_data_range2.xlsx'

# Leer el archivo de Excel
df = pd.read_excel(file_path, sheet_name=None)

# Iterar sobre cada hoja en el archivo de Excel
for sheet in df.keys():
    # Verificar si la columna '/resource_monitor/memory_state/total_program_size' existe en la hoja
    if '/resource_monitor/memory_state/total_program_size' in df[sheet].columns:
        # Filtrar filas donde la columna '/resource_monitor/memory_state/total_program_size' no esté vacía
        df[sheet] = df[sheet].dropna(subset=['/resource_monitor/memory_state/total_program_size'])
        # Mantener solo la primera columna y la columna '/resource_monitor/memory_state/total_program_size'
        first_column = df[sheet].columns[0]
        df[sheet] = df[sheet][[first_column, '/resource_monitor/memory_state/total_program_size']]
    else:
        print(f"La hoja '{sheet}' no contiene la columna seleccionada. Se omitirá esta hoja.")

# Guardar el archivo de Excel limpio
output_path = r'C:\Users\tsvil\Downloads\PLOT\limpio_PLOT_ISOLATED_T_data_range2.xlsx'
with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
    for sheet, data in df.items():
        data.to_excel(writer, sheet_name=sheet, index=False)

print(f'Archivo limpio guardado en: {output_path}')

