# Importar las bibliotecas necesarias
import heapq  # para manejar colas de prioridad
import matplotlib.pyplot as plt  # Para graficar
import networkx as nx  # Para trabajar con grafos

class Transportesdelllano:
    def __init__(self):
        # Inicialización del grafo de conexiones entre estaciones
        self.grafo = {}

    def agregar_conexion(self, origen, destino, tiempo_viaje):
        # Agregar una conexión entre dos estaciones con su respectivo tiempo de viaje
        if origen not in self.grafo:
            self.grafo[origen] = []
        self.grafo[origen].append((destino, tiempo_viaje))

        if destino not in self.grafo:
            self.grafo[destino] = []
        self.grafo[destino].append((origen, tiempo_viaje))