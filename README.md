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
  <<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/56e1f31c-926d-441f-b378-a054c7a0f92b" />
</p>

El tiempo de ejecución total es la métrica principal que muestra la velocidad bruta de cada método. La tabla y el gráfico evidencian claramente que el Cargador Asíncrono (Asyncio) es el más rápido con un tiempo de 1.036 segundos, demostrando su eficiencia superior para tareas de E/S. En contraste, el Cargador Secuencial tardó casi 50 veces más, lo que subraya la importancia de la concurrencia para optimizar el rendimiento.

## Velocidad promedio por imagen (s/img)

Este indicador desglosa el tiempo total para mostrar la eficiencia a nivel micro de cada método. Al dividir el tiempo de ejecución total entre las 151 imágenes, podemos ver que el Cargador Asíncrono procesó cada imagen en solo 0.0068 segundos en promedio, confirmando que es el más ágil. Este dato refuerza la conclusión de que este método es ideal para el manejo de múltiples tareas de red.

En la siguiente tabla se puede evidenciar el tiempo unitario por carga de imagen:

| Método                 | Tiempo Total (s) |
| :--------------------- | :--------------- |
| **Secuencial**         | 0.3288           |
| **Threading**          | 0.0422           |
| **Multiprocesamiento** | 0.0676           |
| **Asyncio**            | 0.0068            |

## Uso de CPU y RAM (%)

Medir la CPU y la RAM resulta ser de gran importancia para terminar de entender los problemas I/O bound y CPU bound. Pues con esto observamos finalmente que este problema es I/O y en la generalidad podríamos decir:

Asyncio (Corredor Ágil): Es el campeón para tareas I/O-Bound. En la carrera de Pokémon, Asyncio demostró una velocidad superior porque su modelo de un solo hilo y sus "corutinas" le permiten manejar miles de conexiones concurrentes sin generar la sobrecarga de múltiples hilos o procesos. Su uso de CPU es bajo porque, en lugar de esperar de forma inactiva, "cede" el control a otras tareas mientras espera que se complete la descarga. Esto se traduce en un consumo mínimo de CPU, lo que lo hace ideal para aplicaciones web, APIs o la descarga masiva de datos.

Threading (Equipo de Multirrea): Este método también es muy efectivo para tareas I/O-Bound. Cada hilo puede manejar una descarga por separado, lo que reduce el tiempo de espera total. Sin embargo, a diferencia de Asyncio, la creación y gestión de hilos tiene una sobrecarga de sistema ("overhead"). Medir la CPU con Threading nos ayuda a ver esta sobrecarga, que aunque es menor que la de Multiprocesamiento, sigue siendo más alta que la de Asyncio.

Multiprocesamiento (Central de Múltiples Núcleos): Este método es el ideal para tareas CPU-Bound. Al crear un proceso completamente nuevo para cada tarea, puede usar múltiples núcleos del procesador al mismo tiempo. En la carrera de Pokémon (que es I/O-Bound), Multiprocesamiento no fue el más rápido porque la creación de procesos es "cara" y no se beneficia del tiempo de espera de las descargas. Sin embargo, si la carrera hubiera sido sobre el procesamiento de imágenes, este método habría superado a los demás, ya que la medición de CPU mostraría un uso intensivo y eficiente de todos los núcleos disponibles.

Secuencial (Tortuga): Este método, al no ser concurrente, no se beneficia del tiempo de inactividad de la CPU durante las operaciones de I/O. El procesador simplemente espera a que cada descarga termine antes de pasar a la siguiente, lo que se refleja en un tiempo de ejecución extremadamente lento y un uso de CPU ineficiente.

En resumen, la medición de CPU no solo valida los resultados de tiempo, sino que también nos ayuda a entender la naturaleza fundamental de la tarea y a elegir la herramienta de concurrencia adecuada. En esta tabla se pueden evidenciar la ejecución de la CPU en los diferentes ejercicios:

| Proceso                          | Threading | Multiprocessing | asyncio | Sequential |
|----------------------------------|-----------|-----------------|---------|------------|
| Uso de CPU (por 1 CPU)           | 28.67%    | 0.40%           | 33.91%  | 4.61%      |
| Uso de CPU (sobre todos los núcleos) | 2.39%     | 0.03%           | 2.83%   | 0.38%      |
| Pico de RAM (RSS) (MB)           | 77.12     | 73.02           | 123.94  | 74.42      |

## Indicador lúdico

<img width="436" height="431" alt="image" src="https://github.com/user-attachments/assets/8013b7ef-b8d6-42a8-807e-049d098b355a" />


La imagen es una comparación visual de dos tipos de problemas: I/O-bound y CPU-bound, utilizando una analogía con el mundo de Pokémon. La imagen se divide en dos secciones verticales.

En la parte izquierda, etiquetada como "I/O-bound", se ilustra una carrera. Esta sección representa tareas que pasan la mayor parte del tiempo esperando a que se complete una operación de entrada/salida (como leer un archivo o una red).

Sequential: Un Pokémon Espeon intenta mover una Pokébola con gran dificultad, simbolizando un proceso lento y secuencial, donde solo se puede trabajar en una tarea a la vez.

Threading: Dos Pokémon Machoke colaboran para mover varias Pokébolas, mostrando cómo el threading (hilos de ejecución) permite realizar múltiples tareas de E/S de forma concurrente, mejorando el rendimiento.

Asyncio: Un Pokémon Eevee corre por delante del resto, con varias Pokébolas suspendidas en el aire detrás de él, lo que representa la velocidad y eficiencia de asyncio para gestionar múltiples operaciones de E/S sin bloquearse.

En la parte derecha, etiquetada como "CPU-bound", se muestra un levantamiento de pesas. Esta sección representa tareas que requieren una gran cantidad de procesamiento de la CPU, como cálculos complejos.

Sequential: Un Pokémon Machoke y un Torkoal levantan pesas pesadas, cada uno por su cuenta. Esto simboliza un proceso secuencial donde cada tarea se completa en un solo núcleo de la CPU.

Threading / Asyncio: Dos Pokémon Machamp levantan pesas aún más grandes, mostrando cómo el threading y asyncio pueden manejar tareas intensivas en CPU, pero con sus limitaciones. Un tercer Machamp, representado por un Gengar, levanta una roca aún más grande, simbolizando que el multiprocessing es superior para tareas que necesitan utilizar múltiples núcleos de la CPU.

Multiprocessing: Un Pokémon Gengar levanta una enorme roca con la etiqueta "Multiprocessing CPU Core", lo que indica que esta es la mejor solución para problemas CPU-bound, ya que puede distribuir la carga de trabajo entre múltiples núcleos de la CPU para un rendimiento máximo.

En resumen, la imagen utiliza una metáfora de carrera y levantamiento de pesas para explicar de manera intuitiva cuándo usar Asyncio (para I/O-bound) y cuándo usar Multiprocessing (para CPU-bound), mientras que Threading se posiciona como una opción intermedia o con limitaciones en ambos escenarios.
---

## 🏆 Análisis y Veredicto

- **El ganador de la carrera (I/O bound)**: **Asyncio** demostró ser el más rápido en esta carrera, lo que confirma su superioridad para tareas de E/S intensivas, como la descarga de múltiples archivos desde la web.  
- **El competidor más fuerte (CPU Bound)**: **Multiprocessing" es el método que tiene mayor utilidad para este tipo de problemas. 
- **La línea base**: El método **Secuencial** nos sirve como punto de referencia para entender la ganancia de rendimiento que ofrecen las otras técnicas.  

En conclusión, la elección del método de concurrencia depende de la naturaleza de la tarea. Para tareas de red y E/S como esta, **Asyncio** es la mejor opción.
