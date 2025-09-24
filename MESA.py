from mesa import Agent, Model
from mesa.time import RandomActivation
import numpy as np

class Cliente(Agent):
    """Agente que representa a un cliente en el sistema."""
    def __init__(self, id_cliente, modelo, tiempo_llegada):
        super().__init__(id_cliente, modelo)
        self.llegada = tiempo_llegada
        self.inicio = None
        self.fin = None

    def step(self):
        # Los clientes no hacen nada por sí mismos,
        # su comportamiento depende del servidor.
        pass

class Servidor(Agent):
    """Agente servidor que atiende a los clientes."""
    def __init__(self, id_servidor, modelo, tasa_mu):
        super().__init__(id_servidor, modelo)
        self.mu = tasa_mu
        self.libre = True
        self.atendiendo = None
        self.tiempo_restante = 0

    def step(self):
        # Si está ocupado, procesar servicio
        if not self.libre:
            self.tiempo_restante -= 1
            if self.tiempo_restante <= 0:
                self.atendiendo.fin = self.model.reloj
                self.model.terminados.append(self.atendiendo)
                self.atendiendo = None
                self.libre = True

        # Si está libre, tomar un cliente de la cola
        if self.libre and self.model.cola:
            cliente = self.model.cola.pop(0)
            cliente.inicio = self.model.reloj
            self.atendiendo = cliente
            self.libre = False
            self.tiempo_restante = np.random.exponential(1 / self.mu)

class SistemaColas(Model):
    """Modelo M/M/1 con simulación discreta."""
    def __init__(self, tasa_lambda, tasa_mu, pasos_max):
        super().__init__()
        self.lambd = tasa_lambda
        self.mu = tasa_mu
        self.servidor = Servidor(0, self, tasa_mu)
        self.schedule = RandomActivation(self)
        self.schedule.add(self.servidor)
        self.cola = []
        self.terminados = []
        self.reloj = 0
        self.id_actual = 1
        self.limite = pasos_max

    def llegada_cliente(self):
        """Generar llegada según probabilidad de Poisson."""
        if np.random.rand() < self.lambd:
            nuevo = Cliente(self.id_actual, self, self.reloj)
            self.schedule.add(nuevo)
            self.cola.append(nuevo)
            self.id_actual += 1

    def step(self):
        self.llegada_cliente()
        self.schedule.step()
        self.reloj += 1

    def run(self):
        while self.reloj < self.limite:
            self.step()

        if not self.terminados:
            return {"N_s": 0, "N_w": 0, "T_s": 0, "T_w": 0, "Rho": 0}

        # Métricas del sistema
        tiempos_sistema = [c.fin - c.llegada for c in self.terminados]
        tiempos_cola = [c.inicio - c.llegada for c in self.terminados]

        T_s = np.mean(tiempos_sistema)
        T_w = np.mean(tiempos_cola)
        N_s = T_s * self.lambd
        N_w = T_w * self.lambd
        utilizacion = len([c for c in self.terminados if c.inicio]) / self.limite

        return {
            "N_s": N_s,
            "N_w": N_w,
            "T_s": T_s,
            "T_w": T_w,
            "Rho": utilizacion
        }

# Ejemplo de ejecución
if __name__ == "__main__":
    modelo = SistemaColas(tasa_lambda=0.5, tasa_mu=1.0, pasos_max=10000)
    resultados = modelo.run()
    print("Resultados de la simulación:")
    print(resultados)
