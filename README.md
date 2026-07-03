# Parcial Práctico

Este repositorio contiene la solución en **Python 3** para el problema **"Tree: Top View"** y ... de HackerRank, correspondiente a la sección del parcial práctico 2.

## Tree: Top View

Este programa imprime la **vista superior (Top View)** de un árbol binario de búsqueda (Binary Search Tree - BST).

La vista superior corresponde al conjunto de nodos que son visibles cuando el árbol se observa desde arriba. Para obtenerla, el algoritmo realiza un recorrido por niveles (Breadth-First Search - BFS), registrando el primer nodo encontrado para cada distancia horizontal respecto a la raíz.

## Cómo poner a funcionar el programa

Existen dos formas de ejecutar y probar este código:

### Opción 1: Ejecución Directa en HackerRank (Recomendado)

1. Copia el código correspondiente a la función `topView(root)` de este repositorio (incluyendo `from collections import deque`).
2. Ve al problema **Tree: Top View** en HackerRank.
3. Selecciona **Python 3** como lenguaje en el editor de HackerRank.
4. Pega el código dentro del editor, respetando la estructura proporcionada por HackerRank.
5. Presiona el botón **"Submit Code"**. El programa ejecutará correctamente todos los casos de prueba.

---

### Opción 2: Ejecución Local en Visual Studio Code

Sigue estos pasos para clonar el proyecto y ejecutarlo directamente en tu computador.

#### 1. Clonar el repositorio desde VS Code

* Abre Visual Studio Code.
* Presiona `Ctrl + Shift + P` (o `Cmd + Shift + P` en Mac).
* Escribe **Git: Clone**.
* Pega la dirección del repositorio:

```text
https://github.com/LauraBernal18/Parcial2ADA.git
```

* Selecciona la carpeta donde deseas guardar el proyecto.

#### 2. Abrir el proyecto

Cuando Visual Studio Code muestre la notificación de apertura del repositorio, selecciona **Open**.

#### 3. Ejecutar el programa

* Abre el archivo `solucion.py`.
* Verifica que tengas instalada la extensión oficial de Python para Visual Studio Code.
* Ejecuta el programa presionando el botón **Run Python File** ubicado en la parte superior derecha o haciendo clic derecho sobre el archivo y seleccionando **Run Python File in Terminal**.

#### 4. Ingreso de datos de prueba

La terminal integrada solicitará los datos de entrada.

Puedes copiar y pegar el siguiente ejemplo:

```text
6
1 2 5 3 6 4
```

#### 5. Verificar el resultado

El programa imprimirá automáticamente la vista superior del árbol.

Para el ejemplo anterior, la salida será:

```text
1 2 5 6
```

---