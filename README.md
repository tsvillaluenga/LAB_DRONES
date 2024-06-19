# LAB_DRONES

## Tareas realizadas hasta el momento
- Creación de repositorio Github
- Preparación de partición Ubuntu 22.04 y entorno de trabajo (ROS2 Humble, Gacebo, Aerostack versión binaria)
- Nociones básicas de arquitectura de Aerostack
- Asistencia a vuelos reales X13 - 10:30 (Exhibición) y J14 - 11:30 (Curso de drones)
- Realización de ejemplos básicos de simulación con Gacebo y Aerostack, con ayuda de la "keyboard teleoperation interface"
- Estudio de MOnitorización de recursos con behaviors
- Migración keyboard de Aerostack a RQt

<br>


## Problemas observados tras ejecucion de Aerostack binario
- Problema con "keyboard teleoperation interface" (solucionado):
  
  1/ crearte un workspace para aerostack2 (as2_ws) y clonarte nuestro repo: https://github.com/aerostack2/aerostack2.git
  
  2/ Antes de compilar, BORRAR TODAS LAS CARPETAS MENOS: as2_cli, as2_python_api, docker.

- Movimientos tras hover --> guarda anterior movimiento durante un instante y después toma el nuevo valor
- Movimiento tras bloqueo --> Cuando está bloqueado para configuración, parece que se guardan en la cola los movimientos indicados por teclado, mientras tanto el dron no se mueve. Pero al cerrar la ventana de configuración, se realizan todos los movimientos indicados secuencialmente. Parece como si los guardase en un buffer cuando no está activo, para realizarlos una vez lo esté.


- Ejercicio "Simple Gazebo Example": mission_planner.py no se ejecuta bien, problemas con el json?
- Ejercicio "Crazyflie Gates Example": mission.py -s no funciona bien, no realiza el movimiento esperado (error: goal rejected)
  
  ![image](https://github.com/tsvillaluenga/LAB_DRONES/assets/47925585/a1af5257-dbc0-4ef9-94c7-46c4bfc50abc)


<br>


## Trabajo de asignatura ROS2 con Aerostack2
### Problemas
- No he podido acceder a los valores de posición del topic /groud_truth, /self_location ni ninguno relacionado con "pose" o "twist". Esto hace que sea más complicado predecir la orientación del dron.
- No he podido utilizar las clases "Mission", "Mission_interpreter" ni "Drone_interface" --> he utilizado directamente la clase "drone_interface_teleop" para los movimientos del dron
- Ejecución de un archivo .sdf junto a la lógica actual del archivo .json

### Videos del funcionamiento

[![Alt text](https://img.youtube.com/vi/configuroweb/0.jpg)](https://www.youtube.com/watch?v=w7MFQtqwtfY)

[![Alt text](https://img.youtube.com/vi/configuroweb/0.jpg)](https://www.youtube.com/watch?v=6oc16JxaSMs)


<br>
<br>


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



<br>
<br>


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


<br>
<br>

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






<br>
<br>
<br>
<br>

## Monitorización recursos - Datos obtenidos
### Composable behaviors

#### MISSION (mission.py)
![image](https://github.com/tsvillaluenga/LAB_DRONES/assets/47925585/2952bb5f-e98f-4260-ad0e-96197feb5b5c)
<br>

**Tiempo de ejecución de mission.py inicio y fin:**
A partir de las siguientes gráficas se puede observar el tiempo de ejecución necesario a la hora de ejecutar el archivo mission.py.


![image](https://github.com/tsvillaluenga/LAB_DRONES/assets/47925585/85fa2971-e8ec-469e-ada6-a764cc77e006)
![image](https://github.com/tsvillaluenga/LAB_DRONES/assets/47925585/241d056c-a437-44a1-974f-5fb6ffaace16)
![image](https://github.com/tsvillaluenga/LAB_DRONES/assets/47925585/927a8356-d89e-4fb9-bcbc-648eca6fce0d)
![image](https://github.com/tsvillaluenga/LAB_DRONES/assets/47925585/26ff80ad-4eb3-45d4-bfaf-5c1a803a0a9c)
(A esta última gráfica no se le ha encontrado aún el sentido relativo al proceso)

<br>

**USO DE RECURSOS:**
Tamaño de memoria utilizado durante ejecución del programa.


![image](https://github.com/tsvillaluenga/LAB_DRONES/assets/47925585/57c917a4-df86-4df0-928c-ae3e4a2210ae)
![image](https://github.com/tsvillaluenga/LAB_DRONES/assets/47925585/7e23b2a2-0fb0-4614-8265-e53b48ed93b8)


---------------------------------------------------------------------
![image](https://github.com/tsvillaluenga/LAB_DRONES/assets/47925585/e52b8804-6914-4c09-9447-2892329986b8)
![image](https://github.com/tsvillaluenga/LAB_DRONES/assets/47925585/d5c5bf38-4fe4-4145-9a15-fc9f23e79c2a)
![image](https://github.com/tsvillaluenga/LAB_DRONES/assets/47925585/3dae004a-8504-4288-b12e-5a1309040131)
![image](https://github.com/tsvillaluenga/LAB_DRONES/assets/47925585/e3096efb-6582-4a5e-8ed4-d8aae3177773)

<br>

### Conclusión

No existen diferencias de uso de memoria a la hora de ejecutar un behavior u otro, el uso de memoria durante la ejecución es constante. Habrá que comprobar su uso de memoria usando diferentes caracteristicas para comprobar cuales proporcionan mejor rendimiento. 










<br>
<br>
<br>
<br>

## Standalone nodes -> Composable nodes
**Referencias a tener en cuenta:**
https://docs.ros.org/en/humble/Tutorials/Intermediate/Writing-a-Composable-Node.html
https://docs.ros.org/en/humble/How-To-Guides/Launching-composable-nodes.html
<br>

Se ha provado con varios nodos (state_estimator, motion_controller,etc.) y finalmente sale siempre el mismo mensaje al ejecutar cada launch individualmente: *_(Ejemplo para State_Estimator)_*:
``` Failed to load node 'StateEstimator' of type 'StateEstimator' in container 'container': Could not find requested resource in ament index ```
<br>

* Se ha probado ha crear un nuevo container dentro del nodo pero sigue apareciendo el problema. **El container se crea correctamente, lo que no se crea es el composable node**. 
* Se ha probado tambien a crear primero el composable node y después el container que lo contenga, pero el error persiste. 
* Se han seguido los pasos del tutorial https://docs.ros.org/en/humble/Tutorials/Intermediate/Writing-a-Composable-Node.html, pero no cambia la forma de actuar en su ejecución.
<br>

Eejmplo de código implementado en en launch:
```def generate_launch_description():
    """ Returns the launch description """

    cnode = ComposableNode(
        package='as2_state_estimator',
        plugin='StateEstimator',
        name='StateEstimator',
        namespace='drone0',
        parameters=[{
            'namespace':'drone0',
            'plugin_name':'ground_truth',
            'use_sim_time':'true',
            'plugin_config_file':'sim_config/state_estimator_config_file.yaml',
            'base_frame':'base_link',
            'global_ref_frame':'earth',
            'odom_frame':'odom',
            'map_frame':'map'
        }]
    )

    container = ComposableNodeContainer(
        name='hola',
        namespace='drone0',
        package='rclcpp_components',
        executable='component_container',
        composable_node_descriptions=[cnode],
        output='screen',
    )

    launch_description = LaunchDescription([container])

    return launch_description
```
<br>

Código añadido a *_state_estimator.cpp_*:
```
#include "rclcpp_components/register_node_macro.hpp"

// Register the component with class_loader.
// This acts as a sort of entry point, allowing the component to be discoverable when its library
// is being loaded into a running process.
RCLCPP_COMPONENTS_REGISTER_NODE(StateEstimator)
```
<br>

Código añadido a CMake:
```
# Components
find_package(rclcpp_components REQUIRED)
add_library(estimator_component SHARED
  src/state_estimator.cpp
)
ament_target_dependencies(estimator_component ${PROJECT_DEPENDENCIES})
rclcpp_components_register_nodes(estimator_component "StateEstimator")

ament_export_targets(export_estimator_component)
install(TARGETS estimator_component
        EXPORT export_estimator_component
        ARCHIVE DESTINATION lib
        LIBRARY DESTINATION lib
        RUNTIME DESTINATION bin
)
```
<br>

Código añadido a *_package.xml_*:
``` <depend>rclcpp_components</depend> ```


<br>
<br>
<br>

### Solución:
https://docs.ros.org/en/humble/Tutorials/Intermediate/Composition.html

**En cpp:**
```
NombreClase::NombreClase(const rclcpp::NodeOptions & options) : Node("NombreClase", options)
```
En el caso en el que la inialización original de la clase del tipo *rclcpp::NodeOptions* tenga algún valor concreto, mover dicha inicialización al archivo **.hpp** como valor por defecto.
<br>
Al final:
```
#include "rclcpp_components/register_node_macro.hpp"

// Register the component with class_loader.
// This acts as a sort of entry point, allowing the component to be discoverable when its library
// is being loaded into a running process.
RCLCPP_COMPONENTS_REGISTER_NODE(NombreClase)    --> Sustituir NombreClase!!!!!!!!!!!!!!
```
<br>

**En hpp:**
```NombreClase(const rclcpp::NodeOptions & options = rclcpp::NodeOptions());     //Constructor ```
En el caso en el que el constructor del **.cpp** disponga de una inicializacion del tipo no vacía, sustituir en esta definicion del Constructor de la clase el ``` = rclcpp::NodeOptions()```por ``` = InicializacionDelCPP```

<br>

**En CMake:** 
Añadir `rclcpp_components` en:
```
# find dependencies
set(PROJECT_DEPENDENCIES
  ament_cmake
  rclcpp
  pluginlib
  as2_core
  nav_msgs
  geometry_msgs
  tf2
  tf2_ros
  rclcpp_components
)
```
<br>

```
# Components
add_library(gazebo_platform_component SHARED  //Nombre que se le da al componente
  src/gazebo_platform.cpp      //Ruta .cpp
)
ament_target_dependencies(gazebo_platform_component ${PROJECT_DEPENDENCIES})
rclcpp_components_register_node(
  gazebo_platform_component
  PLUGIN "gazebo_platform::GazeboPlatform"    //Nombre de la clase de cpp. Si namespace: `nombre_namespace::NombreClase`, si no `NombreClase`.
  EXECUTABLE gazebo_platform    //Nombre de clase searado por _
)

ament_export_targets(export_gazebo_platform_component)
install(TARGETS gazebo_platform_component
        EXPORT export_gazebo_platform_component
        ARCHIVE DESTINATION lib
        LIBRARY DESTINATION lib
        RUNTIME DESTINATION bin
)

```

<br>

**En *_package.xml_***:``` <depend>rclcpp_components</depend> ```

<br>

**En código:** Mantener todos los *FindPackageShare* y asociarlos en el diccionario de parámetros (es necesaria la asociación dinámica).
<br>
**EJECUTAR:** ```as2 build nombre_del_paquete```
<br>
<br>

- [x] platform
- [x] behaviors
- [x] state estimator
- [x] controller
- [ ] viewer

<br>
<br>













##### SOLUCIÓN NO LECTURA DE PARÁMETROS:
Ver pull request " as2 nodes to components #503" de aerostack --> commits "10f734cd5f4b7ee9ce2e6964a8e52f6cfd662afa" y "c388ba4e74406f0d21e2ff1f03a831975e495f76" (de "@pariaspe").




<br>
<br>
############################################################################################################################################################################################################################################

**Crear contenedor con nombre y namespace desde terminal**
`ros2 run rclcpp_components component_container --ros-args -r __node:=aerostack2 -r __ns:=/drone0`

############################################################################################################################################################################################################################################






<br>
<br>

### Monitorización de composable nodes: 

lanzo missión --> ![image](https://github.com/tsvillaluenga/LAB_DRONES/assets/47925585/1cc2fb39-edd1-4ef7-b48a-ba735356ba81) --> otra terminal: `ros2 run topnode resource_monitor` --> `ros2 component load /drone0/container topnode ResourceMonitorNode
`lo que devolverá `"Loaded component 8 into '/drone0/container' container node as '/resource_monitor'"` --> ![image](https://github.com/tsvillaluenga/LAB_DRONES/assets/47925585/c4b6a20d-54e1-4108-a2bb-dbf86c2f99a1) (igual hay que ejecutar 2 veces el código anterior) --> `ros2 lifecycle set /resource_monitor configure MODO` + `ros2 lifecycle set /resource_monitor activate MODO` --> ABRO PLOTJUGGLER (ros2 run plotjuggler plotjuggler) --> Selecciono: 4x"behavior_status" (de cada behavior) + "resource_monitor" --> lanzo mission.py 


##### PROBLEMAS EJECUTANDO MISSION.py:
platform --> ERROR. Se queda bloqueado en Takeoff y no sigue ejecutando (el Takeoff lo hace)

state_estimator --> ERROR. Se queda bloqueado en Takeoff y no sigue ejecutando (el Takeoff lo hace)

controller --> ERROR. No lee los parámetros cuando utilizamos el `LaunchConfigurationEquals('container', 'aerostack2')`

behaviors --> GOOD si introducimos path completo en session de mission.py



**ADICIONAL:** Se estan creando containers cada vez, por lo que hay que hacer que se cree si no existe y que se inserte el nodo en el container si este existe.






<br>
<br>
<br>
<br>

RESPUESTA MISSION NORMAL:

![image](https://github.com/tsvillaluenga/LAB_DRONES/assets/47925585/38311531-a124-412a-96db-9901c96e986f)

![image](https://github.com/tsvillaluenga/LAB_DRONES/assets/47925585/cdc0f729-8537-4bb6-b70f-8622009b28e5)

![image](https://github.com/tsvillaluenga/LAB_DRONES/assets/47925585/22d187fb-6e4b-4e0d-97ad-ad560721d835)

![image](https://github.com/tsvillaluenga/LAB_DRONES/assets/47925585/051c3124-7cd5-4a59-89c4-1a3e1aa2a8d2)



<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

# Resultados Monitorización
Los picos de la gráfica `/resource_monitor/cpu_memory_usage/cpu_usage/percent` se relacionan con los **instantes de ejecución de** `mission.py` 

<br>

### GLOSARIO:
#### Resident Set Size (RSS)

**Qué es Resident Set Size en Linux?**
Resident Set Size (RSS) en Linux se refiere a la porción de la memoria de un proceso que está retenida en RAM. Esto incluye tanto las secciones de código como de datos de un proceso, pero excluye las páginas que se han intercambiado o las que están solo mapeadas a archivos. Representa la memoria física real que un proceso está usando en un momento dado.

**Qué Produce el Aumento de Resident Set Size en Linux?**
El aumento de RSS en Linux puede ser causado por un mayor uso de memoria física por parte del proceso. Esto puede ocurrir debido a:
- Incremento en la cantidad de datos que el proceso maneja.
- Carga de más librerías o módulos.
- Ejecución de más hilos o subprocesos que requieren memoria adicional.

#### Shared Memory

**Qué es Shared Memory en Linux?**
La memoria compartida en Linux es un segmento de memoria que puede ser accedido por múltiples procesos. Permite que diferentes procesos se comuniquen entre sí leyendo y escribiendo en un espacio de memoria común. Esto se utiliza para la comunicación entre procesos (IPC) para lograr un intercambio de datos de alto rendimiento.

**Qué Produce el Aumento de Shared Memory en Linux?**
El aumento de la memoria compartida puede ser causado por:
- Más procesos utilizando segmentos de memoria compartida para comunicarse.
- Incremento en el tamaño de los datos intercambiados entre procesos.
- Uso de técnicas de IPC (Inter-Process Communication) más intensivas que requieren más espacio de memoria compartida.

#### Virtual Memory

**Qué es Virtual Memory en Linux?**
Toda la memoria en Linux se llama memoria virtual; incluye la memoria física (a menudo llamada RAM) y el espacio de intercambio (swap). La memoria física de un sistema no puede aumentarse a menos que agreguemos más RAM. Sin embargo, la memoria virtual puede aumentarse utilizando espacio de intercambio del disco duro.

**Qué Produce el Aumento de Virtual Memory en Linux?**
El aumento de la memoria virtual puede ser causado por:
- Incremento en el tamaño del programa y sus datos.
- Uso de técnicas de memoria dinámica que reservan más espacio de direcciones virtuales.
- Procesos que mapean archivos grandes en su espacio de direcciones virtuales.

#### Data Size

**Qué es Data Size en Linux?**
El tamaño de datos en Linux se refiere a la cantidad de memoria asignada para el segmento de datos de un proceso. Este segmento incluye datos inicializados y no inicializados (variables globales y estáticas) del proceso. Es distinto del segmento de texto (que contiene el código real) y del segmento de pila (que contiene la pila de llamadas a funciones).

**Qué Produce el Aumento de Data Size en Linux?**
El aumento del tamaño de datos puede ser causado por:
- Definición de más variables globales o estáticas.
- Almacenamiento de más datos en estructuras que residen en el segmento de datos.
- Inicialización de datos con valores más grandes.

#### Program Size

**Qué es Program Size en Linux?**
El tamaño del programa en Linux generalmente se refiere a la cantidad total de memoria requerida por un proceso, lo que incluye todos sus segmentos: texto (código), datos (variables inicializadas y no inicializadas), pila (pila de llamadas a funciones) y heap (memoria asignada dinámicamente).

**Qué Produce el Aumento de Program Size en Linux?**
El aumento del tamaño del programa puede ser causado por:
- Adición de más código (funciones y métodos).
- Inclusión de más librerías o dependencias.
- Incremento en la cantidad de datos estáticos y dinámicos que el programa maneja.


#### CPU usage
CPU utilization represents the amount of work a CPU handles to process resources or manage an operating system's tasks.

---

#### RESOLUCIÓN
Explicación de las variables tenidas en cuenta:
:x:**memory_usage/shared_memory** --- NO --- Memoria que comparten los procesos. COMPARTEN MÁS, MENOS?

:white_check_mark:**memory_usage/virtual_memory** --- MMMMM...BUENO SÍ

:ballot_box_with_check:**memory_usage/max_resident_set_size** --- INTERESANTE* -- Uso de procesos y memoria RAM alocada

:ballot_box_with_check:**memory_usage/percent** --- INTERESANTE* --- Porcentaje de la memoria total que se utiliza. 

:x:**memory_state/data_size** --- NO --- Tamaño de las variables que se utilizan.

:white_check_mark:**memory_state/program_size** --- PRINCIPAL --- Resumen de todo el uso de memoria.

:white_check_mark:**cpu_usage/percent** --- SI --- Porcentaje del uso de la CPU total que se utiliza.

<br>

**Memory Usage Percent vs Resident Set Size**:
RSS se refiere a la cantidad de memoria física (RAM) que un proceso específico está utilizando en un momento dado. Sin embargo, el uso de memoria total del sistema considera la memoria utilizada por todos los procesos en el sistema, así como la memoria usada por el kernel, buffers, cachés y otros componentes del sistema. Por tanto, el Resident Set Size tendrá mucho que ver dentro del Memory Usage Percent, pero no todo.

<br>
<br>
<br>


## Standalone Nodes

## Composable Nodes

### Isolated (use_intra_process_comms = True)
![image](https://github.com/tsvillaluenga/LAB_DRONES/assets/47925585/3616c17b-a639-458e-96c1-343799210d74)
![image](https://github.com/tsvillaluenga/LAB_DRONES/assets/47925585/5518af6d-a05b-4029-b052-617fefba88d4)
![image](https://github.com/tsvillaluenga/LAB_DRONES/assets/47925585/28e1a393-d93b-4838-b585-e40af9baf25d)
![image](https://github.com/tsvillaluenga/LAB_DRONES/assets/47925585/69d8e465-eb9d-4023-ad60-d6d5d9d846ee)
![image](https://github.com/tsvillaluenga/LAB_DRONES/assets/47925585/0cd3d19d-56d3-4aea-b007-ddd7febcdb9f)
![image](https://github.com/tsvillaluenga/LAB_DRONES/assets/47925585/adede43d-9540-4d9e-a615-243d96e6f6e2)
![image](https://github.com/tsvillaluenga/LAB_DRONES/assets/47925585/02da7ad1-a32c-47e8-af16-c7ce3679209f)
![image](https://github.com/tsvillaluenga/LAB_DRONES/assets/47925585/9dec3554-6a60-4e5f-aca2-28b28284735f)

---


### Isolated (use_intra_process_comms = False)
![image](https://github.com/tsvillaluenga/LAB_DRONES/assets/47925585/61eaed28-3acb-4ae0-8a92-01757dd44518)
![image](https://github.com/tsvillaluenga/LAB_DRONES/assets/47925585/5f103845-d193-4e92-81a1-b58ab60be3b0)
![image](https://github.com/tsvillaluenga/LAB_DRONES/assets/47925585/082f6d32-9961-4d08-acee-35f3ad5f5c6b)
![image](https://github.com/tsvillaluenga/LAB_DRONES/assets/47925585/e263a15a-a654-4539-ac06-8b7f3bbf68b0)
![image](https://github.com/tsvillaluenga/LAB_DRONES/assets/47925585/2aac6d07-efd3-404d-91b1-fa2b15a074fe)
![image](https://github.com/tsvillaluenga/LAB_DRONES/assets/47925585/59fbe2c9-098f-4beb-b468-bb71bd2d0f3b)
![image](https://github.com/tsvillaluenga/LAB_DRONES/assets/47925585/6248b3c0-a76f-4425-8666-96f1d8d6479d)
![image](https://github.com/tsvillaluenga/LAB_DRONES/assets/47925585/72b72461-c494-4b9c-b1fb-fab50e47bfaa)

---


### Multithread (use_intra_process_comms = True)
![image](https://github.com/tsvillaluenga/LAB_DRONES/assets/47925585/9d2cf5e1-3e7e-4d94-ba08-922e3d930178)
![image](https://github.com/tsvillaluenga/LAB_DRONES/assets/47925585/d64047ae-eb4a-416b-928d-385303e1068d)
![image](https://github.com/tsvillaluenga/LAB_DRONES/assets/47925585/fcce4975-b3ce-4b65-828b-72f62e769012)
![image](https://github.com/tsvillaluenga/LAB_DRONES/assets/47925585/0e689696-9c5b-4b0a-b5ef-d3ea480f6442)
![image](https://github.com/tsvillaluenga/LAB_DRONES/assets/47925585/954b7a0a-e8cd-4d98-8b58-9f9ccef02f15)
![image](https://github.com/tsvillaluenga/LAB_DRONES/assets/47925585/7e691b12-76aa-4e84-a89e-0e03be4c8a61)
![image](https://github.com/tsvillaluenga/LAB_DRONES/assets/47925585/7e1fe0e7-1dfa-4b60-8976-12e0081a7918)
![image](https://github.com/tsvillaluenga/LAB_DRONES/assets/47925585/91bf187b-c57c-4528-bc6f-b0a20b5ecf39)

---


### Multithread (use_intra_process_comms = False)
![image](https://github.com/tsvillaluenga/LAB_DRONES/assets/47925585/b070c1ea-04fd-405f-8ac6-5db0d0ad680f)
![image](https://github.com/tsvillaluenga/LAB_DRONES/assets/47925585/5712a799-1476-4e35-ad7f-47108adf0afc)
![image](https://github.com/tsvillaluenga/LAB_DRONES/assets/47925585/ebf34ab1-8d34-4d28-9e40-00c4922c90ac)
![image](https://github.com/tsvillaluenga/LAB_DRONES/assets/47925585/262dfcba-50c9-4398-a718-a37f7bc2be4e)
![image](https://github.com/tsvillaluenga/LAB_DRONES/assets/47925585/7c0db4e4-e44b-4b97-9a55-5aab603daf68)
![image](https://github.com/tsvillaluenga/LAB_DRONES/assets/47925585/620fbe30-40fa-4600-a346-67e3c310a42c)
![image](https://github.com/tsvillaluenga/LAB_DRONES/assets/47925585/f6cada04-746b-4d8b-94f2-f7671bcb8037)
![image](https://github.com/tsvillaluenga/LAB_DRONES/assets/47925585/13392c3b-a08f-4125-942e-e01e1f5fa058)

---











