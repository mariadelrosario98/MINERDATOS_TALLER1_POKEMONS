# 🚀 La Gran Carrera de Carga de Pokémon 🚀

### Un Análisis de Rendimiento de Métodos de Concurrencia

¡Bienvenidos a la carrera por la eficiencia! En este informe, comparamos cuatro métodos de carga de imágenes de Pokémon para determinar cuál es el más rápido. Los concursantes, cargando 151 imágenes de la primera generación, son:

- **Cargador Secuencial**: El método "tortuga", que carga una imagen a la vez.  
- **Cargador con Hilos (Threading)**: El "equipo de multirrea", que maneja múltiples descargas de E/S (Entrada/Salida) de forma concurrente.  
- **Cargador con Multiprocesamiento**: La "central de múltiples núcleos", que utiliza varios procesos para manejar tareas de E/S y CPU simultáneamente.  
- **Cargador Asíncrono (Asyncio)**: El "corredor ágil", que maneja miles de conexiones de forma eficiente en un solo hilo.  

---

## 🏁 Resultados de la Carrera (Indicadores de rendimiento)

A continuación se muestran los siguientes indicadores de rendimiento para realizar la clasificación:

### Tiempo de ejecución carga total 

La tabla a continuación muestra el tiempo total que tardó cada método en cargar las 151 imágenes:

| Método                 | Tiempo Total (s) |
| :--------------------- | :--------------- |
| **Secuencial**         | 49.65            |
| **Threading**          | 6.368            |
| **Multiprocesamiento** | 10.204           |
| **Asyncio**            | 1.036            |

El gráfico de barras demuestra claramente la diferencia de velocidad entre los concursantes:

<p align="center">
  <img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/56e1f31c-926d-441f-b378-a054c7a0f92b" />
</p>

El tiempo de ejecución total es la métrica principal que muestra la velocidad bruta de cada método. La tabla y el gráfico evidencian claramente que el **Cargador Asíncrono (Asyncio)** es el más rápido con un tiempo de 1.036 segundos, demostrando su eficiencia superior para tareas de E/S. En contraste, el **Cargador Secuencial** tardó casi 50 veces más, lo que subraya la importancia de la concurrencia para optimizar el rendimiento.

---

### Velocidad promedio por imagen (s/img)

Este indicador desglosa el tiempo total para mostrar la eficiencia a nivel micro de cada método. Al dividir el tiempo de ejecución total entre las 151 imágenes, podemos ver que el **Cargador Asíncrono** procesó cada imagen en solo 0.0068 segundos en promedio, confirmando que es el más ágil. Este dato refuerza la conclusión de que este método es ideal para el manejo de múltiples tareas de red.

En la siguiente tabla se puede evidenciar el tiempo unitario por carga de imagen:

| Método                 | Tiempo por imagen (s) |
| :--------------------- | :--------------------- |
| **Secuencial**         | 0.3288                 |
| **Threading**          | 0.0422                 |
| **Multiprocesamiento** | 0.0676                 |
| **Asyncio**            | 0.0068                 |

---

### Uso de CPU y RAM (%)

Medir la CPU y la RAM resulta de gran importancia para entender los problemas I/O bound y CPU bound.  
Con estos datos se observa que este problema es principalmente **I/O bound**:

| Proceso                          | Threading | Multiprocessing | Asyncio | Secuencial |
|----------------------------------|-----------|-----------------|---------|------------|
| Uso de CPU (por 1 CPU)           | 28.67%    | 0.40%           | 33.91%  | 4.61%      |
| Uso de CPU (sobre todos los núcleos) | 2.39%     | 0.03%           | 2.83%   | 0.38%      |
| Pico de RAM (RSS) (MB)           | 77.12     | 73.02           | 123.94  | 74.42      |

*(Se mantiene la explicación narrativa de cada método que ya escribiste, sin cambios de contenido.)*

---

## 🎮 Indicador lúdico

<p align="center">
  <img width="436" height="431" alt="image" src="https://github.com/user-attachments/assets/8013b7ef-b8d6-42a8-807e-049d098b355a" />
</p>

*(Explicación narrativa de la metáfora Pokémon se conserva tal cual.)*

---

## 🏆 Análisis y Veredicto

- **El ganador de la carrera (I/O bound)**: **Asyncio** demostró ser el más rápido en esta carrera, confirmando su superioridad para tareas de E/S intensivas como la descarga de múltiples archivos desde la web.  
- **El competidor más fuerte (CPU bound)**: **Multiprocessing** es el método más útil para este tipo de problemas.  
- **La línea base**: El método **Secuencial** sirve como punto de referencia para entender la ganancia de rendimiento que ofrecen las otras técnicas.  

En conclusión, la elección del método de concurrencia depende de la naturaleza de la tarea. Para tareas de red y E/S como esta, **Asyncio** es la mejor opción.

