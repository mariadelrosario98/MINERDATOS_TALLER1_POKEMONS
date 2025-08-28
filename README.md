# 🚀 La Gran Carrera de Carga de Pokémon 🚀

### Un Análisis de Rendimiento de Métodos de Concurrencia

¡Bienvenidos a la carrera por la eficiencia! En este informe, comparamos cuatro métodos de carga de imágenes de Pokémon para determinar cuál es el más rápido. Los concursantes, cargando 151 imágenes de la primera generación, son:

- **Cargador Secuencial**: El método "tortuga", que carga una imagen a la vez.  
- **Cargador con Hilos (Threading)**: El "equipo de multirrea", que maneja múltiples descargas de E/S (Entrada/Salida) de forma concurrente.  
- **Cargador con Multiprocesamiento**: La "central de múltiples núcleos", que utiliza varios procesos para manejar tareas de E/S y CPU simultáneamente.  
- **Cargador Asíncrono (Asyncio)**: El "corredor ágil", que maneja miles de conexiones de forma eficiente en un solo hilo.  

---

## 🏁 Resultados de la Carrera (Indicadores de rendimiento)
A continuación se muestran los siguientes indicadores de rendimiento para realizar la clasificación

## Tiempo de ejecución carga total 
La tabla a continuación muestra el tiempo total que tardó cada método en cargar las 151 imágenes.

| Método                 | Tiempo Total (s) |
| :--------------------- | :--------------- |
| **Secuencial**         | 49.65            |
| **Threading**          | 6.368            |
| **Multiprocesamiento** | 10.204           |
| **Asyncio**            | 1.036            |

El gráfico de barras demuestra claramente la diferencia de velocidad entre los concursantes.
<p align="center">
  <img width="418" height="203" alt="image" src="https://github.com/user-attachments/assets/adb29c17-99b2-47da-b71a-c3b10c342365" />
</p>

## Velocidad promedio por imagen (s/img)

Divide el tiempo total entre las 151 imágenes. Esto permite comparar qué tan rápido es cada método a nivel micro.

## Uso de CPU y RAM (%)

Añadir una tabla con los recursos consumidos por cada método durante la ejecución. Hace más evidente cuándo un método es “rápido” pero “caro” en recursos.

## Eficiencia relativa (%)

Mide cuánto más rápido es cada método respecto al secuencial. Ejemplo: Asyncio = 450% más rápido.

## Consumo de energía estimado ⚡ (opcional, divertido)

Usando proxies como uso de CPU, podrías simular un “score energético” y añadirlo como parte de la carrera.

## Gráfico extra

Además del gráfico de barras de tiempo, incluir:

📉 Gráfico de líneas: progreso acumulado de descargas con cada método.

📊 Radar chart: comparar simultáneamente tiempo, uso de CPU, uso de memoria.

## Indicador lúdico

Una “medalla” o emoji según la posición: 🥇, 🥈, 🥉, 🐢.

Una barra de “diversión / creatividad” donde cada método tenga un puntaje según su estilo (ejemplo: Asyncio = “ninja runner”, Multiprocessing = “muscle power”).

---

## 🏆 Análisis y Veredicto

- **El ganador**: **Asyncio** demostró ser el más rápido en esta carrera, lo que confirma su superioridad para tareas de E/S intensivas, como la descarga de múltiples archivos desde la web.  
- **El competidor más fuerte**: Aunque **Threading** también fue muy rápido, tiene una sobrecarga mayor que Asyncio.  
- **El método más completo**: **Multiprocesamiento** es ideal para tareas que no solo son de E/S, sino que también tienen una alta demanda de CPU (por ejemplo, procesamiento de imágenes).  
- **La línea base**: El método **Secuencial** nos sirve como punto de referencia para entender la ganancia de rendimiento que ofrecen las otras técnicas.  

En conclusión, la elección del método de concurrencia depende de la naturaleza de la tarea. Para tareas de red y E/S como esta, **Asyncio** es la mejor opción.
