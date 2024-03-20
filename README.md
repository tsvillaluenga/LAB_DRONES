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
