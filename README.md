# Analisis-Cola-M-M-1-K-Inf
##Descripción General
-Este proyecto analiza el comportamiento de un sistema de colas del tipo M/M/1/K/∞, caracterizado por:
-Proceso de llegadas: Distribución de Poisson con tasa λ
-Tiempos de servicio: Distribución exponencial con tasa μ
-Configuración: Un único servidor con capacidad máxima K
-Política de rechazo: Clientes que llegan con el sistema lleno (n = K) son bloqueados
-La investigación combina modelado matemático de teoría de colas con simulación computacional usando el framework MESA en Python para validar resultados teóricos.

## Objetivos
-Desarrollar el modelo analítico del sistema M/M/1/K/∞
-Calcular métricas de rendimiento teóricas
-Implementar simulación computacional con MESA
-Contrastar resultados teóricos vs simulados

## Modelo Matematico
Probabilidad de sistema vacío
      1 - ρ
P₀ = ————————
     1 - ρᴷ⁺¹
Probabilidad de n clientes:
      (1 - ρ) · ρⁿ
Pₙ = ——————————————,   n = 0, 1, ..., K
       1 - ρᴷ⁺¹

Probabilidad de bloqueo:
      (1 - ρ) · ρᴷ
Pₖ = ——————————————
       1 - ρᴷ⁺¹
Clientes en el sistema:
      ρ · [1 - (K + 1)ρᴷ + Kρᴷ⁺¹]
L = ———————————————————————————————
          (1 - ρ)(1 - ρᴷ⁺¹)

Tiempo en el sistema:
     L
W = —————————
    λ(1 - Pₖ)
Clientes en cola:
Lq = L - (1 - P₀)
Tiempo en cola:
     Lq
Wq = —————————
    λ(1 - Pₖ)


