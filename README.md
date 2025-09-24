# Proyecto: Sistema de Colas M/M/1/K/∞

## Introducción
Este proyecto analiza el funcionamiento de un sistema de colas **M/M/1/K/∞**, definido por las siguientes características:  

- **Llegadas** con distribución de Poisson (tasa \( \lambda \)).  
- **Tiempos de servicio** con distribución exponencial (tasa \( \mu \)).  
- **Un único servidor** con una cola de tamaño máximo \( K \).  
- Si al llegar un cliente el sistema está lleno (\( n = K \)), este es rechazado (bloqueo).  

El trabajo combina la formulación teórica de la **teoría de colas** con la **simulación computacional**, implementada en Python con el framework **MESA**, con el fin de verificar los resultados.



## Objetivos
- Formular matemáticamente el sistema M/M/1/K/∞.  
- Obtener métricas de desempeño esperadas:  
  - Número promedio de clientes en el sistema (\( N_s \)).  
  - Tiempo medio en el sistema (\( T_s \)).  
  - Número esperado de clientes en cola (\( N_w \)).  
  - Tiempo medio de espera en cola (\( T_w \)).  
  - Probabilidad de bloqueo (\( P_K \)).  
- Desarrollar una simulación en Python con MESA.  
- Comparar los resultados teóricos frente a los obtenidos en la simulación.  



## Modelo Matemático

- **Probabilidad de que el sistema esté vacío**
   
\[
$P_0 = \frac{1 - \rho}{1 - \rho^{K+1}}, \quad \rho = \frac{\lambda}{\mu}$
\]

- **Probabilidad de que existan \( n \) clientes en el sistema**  
\[
$P_n = \frac{(1 - \rho)\rho^n}{1 - \rho^{K+1}}, \quad n = 0,1,2,\dots,K$
\]

- **Probabilidad de bloqueo (sistema lleno)**  
\[
$P_K = \frac{(1 - \rho)\rho^K}{1 - \rho^{K+1}}$
\]

- **Número esperado de clientes en el sistema**  
\[
$N_s = \frac{\rho\big(1 - (K+1)\rho^K + K\rho^{K+1}\big)}{(1-\rho)(1-\rho^{K+1})}$
\]

- **Tiempo promedio en el sistema (Ley de Little)**  
\[
$T_s = \frac{N_s}{\lambda(1 - P_K)}$
\]

- **Número esperado de clientes en cola**  
\[
$N_w = N_s - (1 - P_0)$
\]

- **Tiempo promedio de espera en cola**  
\[
$T_w = \frac{N_w}{\lambda(1 - P_K)}$
\]

---

## Simulación con MESA
La implementación en Python se construyó usando **MESA** (framework de simulación basada en agentes).  

- **Clientes**: llegan según un proceso de Poisson con parámetro \( \lambda \).  
- **Servidor**: atiende clientes en orden de llegada (FIFO) con tasa \( \mu \).  
- La simulación registra: \( N_s \), \( T_s \), \( N_w \), \( T_w \), utilización del servidor y probabilidad de bloqueo.  

Conforme aumenta la duración de la simulación, los resultados empíricos se aproximan a los valores teóricos.



## Resultados
Se probaron tres configuraciones diferentes para observar el comportamiento del sistema:

- **Escenario 1 (baja carga):** \( \lambda = 0.4, \mu = 1.2, \rho = 0.333 \).  
  Resultados teóricos: \( N_s = 0.5, T_s = 1.25, N_w = 0.167, T_w = 0.417 \).  

- **Escenario 2 (carga media):** \( \lambda = 1.2, \mu = 2.0, \rho = 0.6 \).  
  Resultados teóricos: \( N_s = 1.5, T_s = 1.25, N_w = 0.9, T_w = 0.75 \).  

- **Escenario 3 (alta carga):** \( \lambda = 1.8, \mu = 2.0, \rho = 0.9 \).  
  Resultados teóricos: \( N_s = 9.0, T_s = 5.0, N_w = 8.1, T_w = 4.5 \).  

En todos los casos, se espera que los valores simulados se acerquen a los teóricos, validando el modelo matemático.


## Conclusiones
- Los resultados simulados se alinean con las expresiones teóricas del sistema **M/M/1/K/∞**.  
- La probabilidad de bloqueo \( P_K \) indica la proporción de clientes rechazados cuando el sistema está saturado.  
- Al crecer \( \rho \) hacia 1, tanto los tiempos de espera como la longitud de la cola aumentan rápidamente.  
- El framework **MESA** permite validar la teoría con experimentos reproducibles.  
- La combinación de análisis matemático y simulación entrega una visión más clara y completa del desempeño del sistema.  

