# Modelo Matemático – Sistema de Colas M/M/1/K/∞

## Introducción
Este documento presenta el análisis teórico de un sistema de colas **M/M/1/K/∞**, con el objetivo de calcular métricas de desempeño como el número promedio de clientes en el sistema, tiempos de espera y utilización del servidor.  

El sistema se caracteriza por:
- **Llegadas** con distribución de Poisson, tasa \( \lambda \).  
- **Servicios** con distribución exponencial, tasa \( \mu \).  
- **Un único servidor**.  
- **Capacidad máxima \( K \)** (si la cola está llena, los clientes son rechazados).  

---

## Fórmulas Matemáticas

- **Utilización del servidor:**

$$
\rho = \frac{\lambda}{\mu}
$$

- **Número esperado de clientes en el sistema:**

$$
N_s = \frac{\rho}{1 - \rho}
$$

- **Tiempo promedio en el sistema (Ley de Little):**

$$
T_s = \frac{N_s}{\lambda}
$$

- **Número esperado de clientes en cola:**

$$
N_w = N_s - \rho
$$

- **Tiempo promedio en la cola:**

$$
T_w = \frac{N_w}{\lambda}
$$

📌 *Nota*: Se asume \( K \to \infty \) (cola infinita), por lo que la probabilidad de bloqueo es \( P_K = 0 \).

---

## Resultados Teóricos

A continuación, se muestran los cálculos para tres configuraciones distintas de \( \lambda \) y \( \mu \):

### 🔹 Escenario 1: Baja carga
- Parámetros: \( \lambda = 0.4 \), \( \mu = 1.2 \)  
- Utilización: \( \rho = 0.333 \)  

Resultados:  
\[
N_s = 0.5, \quad T_s = 1.25, \quad N_w = 0.167, \quad T_w = 0.417
\]

---

### 🔹 Escenario 2: Carga media
- Parámetros: \( \lambda = 1.2 \), \( \mu = 2.0 \)  
- Utilización: \( \rho = 0.6 \)  

Resultados:  
\[
N_s = 1.5, \quad T_s = 1.25, \quad N_w = 0.9, \quad T_w = 0.75
\]

---

### 🔹 Escenario 3: Alta carga
- Parámetros: $\( \lambda = 1.8 \), \( \mu = 2.0 \) $ 
- Utilización: $\( \rho = 0.9 \)  $

Resultados:  
\[
$N_s = 9.0, \quad T_s = 5.0, \quad N_w = 8.1, \quad T_w = 4.5$
\]

---

## Conclusión
- A medida que la **utilización del servidor** (\( \rho \)) se acerca a 1, el tiempo en el sistema y en la cola crecen de forma significativa.  
- En escenarios de baja carga, el sistema opera de forma eficiente con pocos clientes en espera.  
- En condiciones de alta carga, las colas se vuelven largas y los tiempos de espera aumentan drásticamente, lo que refleja el riesgo de saturación del sistema.  
