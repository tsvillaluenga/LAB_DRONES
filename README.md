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
Se han observado 2 métodos:

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


### topnode
Según la teoría es ideal para lo que buscamos. Se deben introducir componentes/nodos en un container y el nodo de análisis monitoriza el uso de los recursos de esos nodos introducidos en el container.

[Github del recurso "topnode"]([https://pages.github.com/](https://github.com/safe-ros/topnode))

En */topnode/topnode/launch* existe un archivo launcher como el del ejemplo de Github mediante el cual se puede realizar la instrumentación del container.
**PROBLEMAS:** No consigo obtener datos visuales de la ejecución de este container como utilizando las aplicaciones anteriores. No entiendo exactamente qué es lo que tendría que salir.
**RESULTADOS:** 
Container:
![image](https://github.com/tsvillaluenga/LAB_DRONES/assets/47925585/65ba5e7f-3ec7-48ab-9832-41a47e688dc1)

Talker publicando, pero ¿Necesita ejecutable para ser monitorizado?¿Qúe ejecutable?:
![image](https://github.com/tsvillaluenga/LAB_DRONES/assets/47925585/6139adb2-958f-435a-8e1d-5497041e58fb)

Monitorizando:
![image](https://github.com/tsvillaluenga/LAB_DRONES/assets/47925585/3a7d034a-cea8-4ced-bb4f-69619dbd5048)





