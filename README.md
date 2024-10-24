[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/9J9TrW2r)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=16642751&assignment_repo_type=AssignmentRepo)
# Práctica 2: Introducción al desarrollo. Ponlo en práctica. 

Apoyate en los siguientes recursos para realizar la práctica:

[Descripción de la práctica](https://revilofe.github.io/section3/u01/practica/EDES-U1.-Practica011/)


---

# Práctica 1.11: Elementos de desarrollo

## Identificación de la Actividad
- **ID de la Actividad:** P 1.11 Elementos del desarrollo: ponlo en práctica
- **Módulo:** `EDES`
- **Unidad de Trabajo:** Und 1
- **Fecha de Creación:** 19/10/2024
- **Fecha de Entrega:** 24/10/2024
- **Alumno:** 
  - **Nombre y Apellidos:** Daniel Villar Guttenberger
  - **Correo electrónico:** dvilgut2404@g.educaand.es
  - **Iniciales del Alumno:** DVG

## Descripción de la Actividad
Evaluar la relación entre software y hardware, clasificar lenguajes de programación y comprender los diferentes procesos de ejecución (compilación, interpretación y máquinas virtuales), utilizando ejemplos de lenguajes interpretados, compilados y que generan código intermedio para su ejecución en una máquina virtual.

## Instrucciones de Compilación y Ejecución
1. **Requisitos Previos:**
   - Python, C y Java
   - Visual Studio Code

2. **Pasos para Compilar el Código:**
   
   Para compilar nuestro programa en C:

   codigo ejecutable:
   ```bash
   gcc programaEnC.c -c programaEnC
   ```

   Para ver el byteCode en java:
   ```bash
   javap -c programaEnJava.java
   ```

   Para compilar nuestro programa en Java:
   ```bash
   javap programaEnJava.java
   ```

3. **Pasos para Ejecutar el Código:**

   Para ejecutar el programa en python:
   ```bash
   python3 bienvenida.py
   ```

   Para ejecutar el programa en C:
   ```bash
   ./programaEnC
   ```

   Para ejecutar el programa en java:
   ```bash
   java programaEnJava
   ```

### Código Fuente

   - [Código fuente C.](src/programaEnC.c) 

   - [Código fuente java.](src/programaEnJava.java)

   - [Código fuente python.](src/programaEnPython.py)


5. Preguntas y Actividades para Evaluar Cada Criterio de Evaluación

   1. Relación entre Software y Hardware
Durante la ejecución de los programas:

Memoria RAM: Los datos (como el nombre del usuario) se almacenan en la RAM. En Python y Java, se utilizan objetos y variables, mientras que en C, se utiliza un arreglo de caracteres.

Procesador: El procesador ejecuta instrucciones. En el caso de C, se compila el código a código máquina, que el procesador puede ejecutar directamente. Para Python y Java, el procesador ejecuta instrucciones a través del intérprete y la máquina virtual respectivamente.

Interacción con periféricos: En todos los lenguajes, se interactúa con la pantalla para mostrar la salida. Esto se realiza a través de las bibliotecas y funciones específicas de cada lenguaje.

   2. Diferenciación entre Código Fuente, Código Objeto y Ejecutable
C: El código fuente se transforma en código objeto mediante un compilador (por ejemplo, gcc). El archivo generado suele tener la extensión .o. Luego, este se enlaza para generar un ejecutable (por ejemplo, a.out).

Python: No se generan archivos intermedios; el intérprete ejecuta directamente el código fuente.

Java: El código fuente se compila a bytecode (archivo .class) mediante el compilador javac. Este bytecode es ejecutado por la JVM (Java Virtual Machine).

   3. Generación de Código Intermedio para Máquinas Virtuales

En Java, el código fuente se compila a bytecode. Este bytecode es un formato intermedio que la JVM interpreta y ejecuta. La máquina virtual proporciona un entorno de ejecución que permite que el mismo bytecode se ejecute en diferentes plataformas, a diferencia de los lenguajes compilados que generan código específico para cada sistema operativo.

   4. Clasificación de Lenguajes de Programación

Lenguaje: Python	Modo de Ejecución: Interpretado	   Nivel de Abstracción: Alto nivel	Paradigma: Imperativo, Orientado a objetos
Lenguaje: C	      Modo de Ejecución: Compilado	      Nivel de Abstracción: Bajo nivel	Paradigma: Imperativo
Lenguaje: Java    Modo de Ejecución: Máquina virtual	Nivel de Abstracción: Alto nivel	Paradigma: Orientado a objetos

Características: Python es fácil de leer y escribir, ideal para desarrollo rápido. C ofrece control bajo nivel y eficiencia. Java combina la facilidad de un alto nivel con portabilidad gracias a la JVM.

   5. Evaluación de Herramientas Utilizadas en el Desarrollo
Python:
Sistema Operativo: Linux
Editor/IDE: Visual Studio Code
Intérprete: Python 3

C:
Sistema Operativo: Linux
Editor/IDE: Visual Studio Code 
Compilador: GCC

6. Entrega

codigos en la carpeta src

![Prueba en python](<Captura desde 2024-10-19 16-58-14.png>)
![Prueba en C](<Captura desde 2024-10-19 16-42-11.png>)

7. Conclusión Final
Comparando los tres lenguajes:

Rendimiento: C es el más rápido, seguido de Java (por la JVM), y Python es el más lento debido a su naturaleza interpretada.
Facilidad de uso: Python es el más accesible, seguido de Java, mientras que C puede ser más complejo debido a su manejo de memoria.
Ventajas y desventajas: Python es flexible y fácil, pero menos eficiente. C ofrece control y velocidad, pero es más propenso a errores de gestión de memoria. Java ofrece portabilidad y seguridad, aunque puede ser más pesado debido a la JVM.
