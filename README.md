# LAB_DRONES

## Tareas realizadas hasta el momento
- Creación de repositorio Github
- Preparación de partición Ubuntu 22.04 y entorno de trabajo (ROS2 Humble, Gacebo, Aerostack versión binaria)
- Nociones básicas de arquitectura de Aerostack
- Asistencia a vuelos reales X13 - 10:30 (Exhibición) y J14 - 11:30 (Curso de drones)
- Realización de ejemplos básicos de simulación con Gacebo y Aerostack, con ayuda de la "keyboard teleoperation interface"


## Problemas observados tras ejecucion de Aerostack binario
- Problema con "keyboard teleoperation interface" (solucionado):
  1/ crearte un workspace para aerostack2 (as2_ws) y clonarte nuestro repo: https://github.com/aerostack2/aerostack2.git
  2/ Antes de compilar, BORRAR TODAS LAS CARPETAS MENOS: as2_cli, as2_python_api, docker.

- Movimientos tras hover --> guarda anterior movimiento durante un instante y después toma el nuevo valor
- Movimiento tras bloqueo --> Cuando está bloqueado para configuración, parece que se guardan en la cola los movimientos indicados por teclado, mientras tanto el dron no se mueve. Pero al cerrar la ventana de configuración, se realizan todos los movimientos indicados secuencialmente. Parece como si los guardase en un buffer cuando no está activo, para realizarlos una vez lo esté.


- Ejercicio "Simple Gazebo Example": mission_planner.py no se ejecuta bien, problemas con el json?
- Ejercicio "Crazyflie Gates Example": mission.py -s no funciona bien, no realiza el movimiento esperado (error: goal rejected)
  
  ![image](https://github.com/tsvillaluenga/LAB_DRONES/assets/47925585/a1af5257-dbc0-4ef9-94c7-46c4bfc50abc)





## Trabajo de asignatura ROS2 con Aerostack2
### Problemas
- No he podido acceder a los valores de posición del topic /groud_truth, /self_location ni ninguno relacionado con "pose" o "twist". Esto hace que sea más complicado predecir la orientación del dron.
- No he podido utilizar las clases "Mission", "Mission_interpreter" ni "Drone_interface" --> he utilizado directamente la clase "drone_interface_teleop" para los movimientos del dron
- Ejecución de un archivo .sdf junto a la lógica actual del archivo .json

### Videos del funcionamiento

[![Alt text](https://img.youtube.com/vi/configuroweb/0.jpg)](https://www.youtube.com/watch?v=w7MFQtqwtfY)

[![Alt text](https://img.youtube.com/vi/configuroweb/0.jpg)](https://www.youtube.com/watch?v=6oc16JxaSMs)





## APUNTES: Nodos ROS2
rclcpp::**spin()** --> Se encarga de mandar acciones/procesos a la cola de ejecución 
executor --> es el encargado de ejecutar/consumir las acciones de la cola

### Tipos de nodos

![image](https://github.com/tsvillaluenga/LAB_DRONES/assets/47925585/97744cf0-247f-4d51-b2cf-d4cc4dca1d07)

**--> Normalmente en los STANDALONE NODES se utiliza un executor por cada nodo, aunque realmente en muchos casos se podría utilizar un mismo executor para ahorrar espacio de memoria reservado para la ejecución (ya que en muchos casos no es necesario grandes frecuencias de cómputo)**

[FALTA AÑADIR BIBLIOGRAFÍA)

#### Composable (CONTAINER - COMPONENT)
Un mismo **executor** para **varios nodos.**

![image](https://github.com/tsvillaluenga/LAB_DRONES/assets/47925585/e03c5761-3f49-4e9b-be6d-b3707c706c80)


[FALTA AÑADIR BIBLIOGRAFÍA)

#### Lifecycle (Máquina de estados)

![image](https://github.com/tsvillaluenga/LAB_DRONES/assets/47925585/04412c4f-3b0c-4e21-951a-a770656d3a0c)

[FALTA AÑADIR BIBLIOGRAFÍA)
https://design.ros2.org/articles/node_lifecycle.html







## Monitorización de recursos
Se han observado varios métodos:


### htop o nmon
Ambos métodos son muy parecidos y tienen capacidad de filtrar por servicios, procesos o nombres. Además existen maneras de grabar los datos obtenidos de la ejecución para un posterior análisis.

#### htop
**Ejecutar:**  `htop`
**Para guardar los datos obtenidos:**  `top -b -n1 > top.txt`
Permite guardar tantas iteraciones como uno quiera modificando el parámetro `-nX` donde `X` será el número de iteraciones que se quieren guardar. Cada iteración se realiza cada en torno 3 segundos.

#### nmon
**Ejecutar:**  `nmon`
**Para guardar los datos obtenidos:**  `nmon -f -s <secs> -c <refreshno>`
Permite recopilar los datos en un archivo. La opción `-`f le dice a nmon que recopile los datos y los coloque en un archivo. Nmon especifica el archivo, que termina en `.nmon` (*CSV Spreadsheet format*). La opción `-s <secs>` le dice a nmon que recopile datos cada <secs> segundos. La opción `-c <refreshno>` le dice a nmon que recopile el número de actualizaciones <refreshno> . El período de tiempo total en el que nmon recopila datos es solo el producto de <secs> y <refreshno>. De todas maneras verdemás parámetros importantes en `ǹmon -h`, ya que debido a la gran cantidad de datos que aporta, hay que filtrar algo más los datos pedidos.

#### Métodos para ROS
-  rosprofiler ([Github del recurso](http://wiki.ros.org/rosprofiler))
-  rqt_top ([Github del recurso](http://wiki.ros.org/rqt_top))
-  rp2_computer_monitor (bastante completa) ([Github del recurso](http://wiki.ros.org/rp2_computer_monitor))
-  cpu_monitor ([Github del recurso](https://github.com/alspitz/cpu_monitor))

#### rotop (ROS 2)
([Github del recurso](https://github.com/iwatake2222/rotop))
Es una herramienta interesante que se asemeja a lo que puede aportar tanto nmon, como top o htop pero de una manera más legible, sencilla y con datos más simples. Además de aportar valores de monitorización de recursos, tambien te los grafica mediante su propia GUI.

**PROBLEMA:** Al ejecutarlo de cualquier manera se obtiene un error. Puede ser debido al ordenador y directamente por que la versión del software está atrasada o sin seguimiento.
```
  File "/home/tsvillaluenga/.local/bin/rotop", line 8, in <module>
    sys.exit(main())
  File "/home/tsvillaluenga/.local/lib/python3.10/site-packages/rotop/rotop.py", line 91, in main
    curses.wrapper(main_curses, args)
  File "/usr/lib/python3.10/curses/__init__.py", line 94, in wrapper
    return func(stdscr, *args, **kwds)
  File "/home/tsvillaluenga/.local/lib/python3.10/site-packages/rotop/rotop.py", line 49, in main_curses
    _ = data_container.run(top_runner, result_show_all_lines, args.num_process)
  File "/home/tsvillaluenga/.local/lib/python3.10/site-packages/rotop/data_container.py", line 62, in run
    self.df_cpu_history = self.sort_df_in_column(self.df_cpu_history)
  File "/home/tsvillaluenga/.local/lib/python3.10/site-packages/rotop/data_container.py", line 75, in sort_df_in_column
    df = df.sort_values(by=len(df)-1, axis=1, ascending=False)
  File "/home/tsvillaluenga/.local/lib/python3.10/site-packages/pandas/core/frame.py", line 7176, in sort_values
    k = self._get_label_or_level_values(by[0], axis=axis)
  File "/home/tsvillaluenga/.local/lib/python3.10/site-packages/pandas/core/generic.py", line 1910, in _get_label_or_level_values
    raise KeyError(key)
KeyError: -1
```





### topnode

([Github del recurso "topnode"](https://github.com/safe-ros/topnode))

Genera un nuevo nodo de ROS 2 que permite monitorizar los recursos de un container. Para ello, debes crear un container, meter los nodos que deseas monitorizar en él e introducir el nodo `/resource_monitor` tambien en el container. Este nodo genera **2 nuevos topics** a partir de los cuales se puede obtener toda la información de monitorización. Los campos que aportan dichos topics son los siguientes:
```
/resource_monitor/cpu_memory_usage
  pid
  cpu_usage
    elapsed_time
    user_mode_time
    total_user_mode_time
    kernel_mode_time
    total_kernel_mode_time
    percent
    load_average
  memory_usage
    max_resident_set_size
    shared_size
    virtual_size
    percent

/resource_monitor/memory_state
  total_program_size
  resident_size
  shared_page_count
  text_size
  lib_size
  data_size
  dirty_pages
```
A partir de estos datos habrá que elegir cuales son los que realmente nos interesan y cuales no.

Para inicial el monitoreo de recursos habrá que configurar primero el nodo `/resource_monitor` mediante un lifecycle. Para ello:
1º/ `ros2 lifecycle set /resource_monitor configure MODO`
2º/ `ros2 lifecycle set /resource_monitor activate MODO`
3º/ `ros2 lifecycle set /resource_monitor deactivate MODO`

OTRO/ `ros2 lifecycle set /resource_monitor shutdown MODO`
OTRO/ `ros2 lifecycle set /resource_monitor clear MODO`

Donde *MODO* puede ser: `--include-hidden-nodes`, `-s`, `--use-sim-time`, `--no-daemon` o `--spin-time`.






