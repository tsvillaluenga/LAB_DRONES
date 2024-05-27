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
- [ ] state estimator
- [x] controller
- [ ] viewer

<br>
<br>

MÉTODO SOLUCIÓN ERROR: (as2 build ...) -->
```
CMake Error at /opt/ros/humble/share/rclcpp_components/cmake/rclcpp_components_register_nodes.cmake:29 (message):
  rclcpp_components_register_nodes() first argument 'as2_alphanumeric_viewer'
  is not a target
Call Stack (most recent call first):
  CMakeLists.txt:58 (rclcpp_components_register_nodes)
```
MÉTODO ANTERIOR A SOLUCIÓN ERROR: (as2 build ... --> GOOD ---> ros2 launch ... -->)
```
ros2 launch /home/tsvillaluenga/aerostack2_ws/src/aerostack2/as2_user_interfaces/as2_alphanumeric_viewer/launch/tsv_alphanumeric_viewer_launch.py
```

```
[INFO] [launch]: All log files can be found below /home/tsvillaluenga/.ros/log/2024-05-26-23-29-00-379845-tsvillaluenga-HP-Pavilion-Laptop-15-cs1xxx-10384
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [component_container-1]: process started with pid [10396]
[component_container-1] [INFO] [1716758941.489346852] [drone0.container]: Load Library: /home/tsvillaluenga/aerostack2_ws/install/as2_alphanumeric_viewer/lib/libalphanumeric_viewer_component.so
[component_container-1] [ERROR] [1716758941.512292078] [drone0.container]: Failed to load library: Could not load library dlopen error: /home/tsvillaluenga/aerostack2_ws/install/as2_alphanumeric_viewer/lib/libalphanumeric_viewer_component.so: undefined symbol: stdscr, at ./src/shared_library.c:99
[ERROR] [launch_ros.actions.load_composable_nodes]: Failed to load node 'AlphanumericViewer' of type 'AlphanumericViewer' in container '/drone0/container': Failed to load library: Could not load library dlopen error: /home/tsvillaluenga/aerostack2_ws/install/as2_alphanumeric_viewer/lib/libalphanumeric_viewer_component.so: undefined symbol: stdscr, at ./src/shared_library.c:99
```
