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

    def encontrar_ruta_optima(self, origen, destino):
        # Inicializar la cola de prioridad (heap) con la tupla inicial
        heap = [(0, origen, [])]  # (costo acumulado, estacion actual, ruta hasta el momento)
        visitados = set()  # Conjunto para mantener registro de estaciones visitadas

        while heap:
            print(heap)
            # Extraer la tupla con menor costo acumulado desde el heap
            costo_acumulado, estacion_actual, ruta = heapq.heappop(heap)
            
            # Verificar si se ha alcanzado el destino
            if estacion_actual == destino:
                return ruta + [destino]  # Devolver la ruta completa hasta el destino

            # Marcar la estación actual como visitada
            if estacion_actual not in visitados:
                visitados.add(estacion_actual)

                # Explorar las conexiones de la estación actual
                for vecino, tiempo_viaje in self.grafo[estacion_actual]:
                    # Verificar si el vecino no ha sido visitado
                    if vecino not in visitados:
                        # Calcular el nuevo costo acumulado y la nueva ruta
                        nuevo_costo = costo_acumulado + tiempo_viaje
                        nueva_ruta = ruta + [estacion_actual]
                        # Agregar la tupla al heap para explorar el vecino
                        heapq.heappush(heap, (nuevo_costo, vecino, nueva_ruta))
                        print(heap)
                                                
      
        return ("NO se encontro ruta")
