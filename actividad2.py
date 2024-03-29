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



    def dibujar_grafo(self):
        # Crear un objeto de grafo dirigido
        G = nx.DiGraph()

        
        # Iterar sobre cada estación y sus conexiones en el grafo
        for estacion, conexiones in self.grafo.items():
            # Agregar cada estación como un nodo al grafo
            G.add_node(estacion)

        # Iterar sobre cada estación y sus conexiones en el grafo
        for estacion, conexiones in self.grafo.items():
            # Iterar sobre cada conexión desde la estación actual
            for conexion in conexiones:
            # Agregar una arista desde la estación actual hacia la estación de destino
            # con un atributo de peso igual al tiempo de viaje
             G.add_edge(estacion, conexion[0], weight=conexion[1])

             
        # Dibujar el grafo
             
        plt.figure(figsize=(20, 8))  # Crear una nueva figura con tamaño personalizado
        pos = nx.spring_layout(G)  # Calcular la disposición de los nodos utilizando el algoritmo spring
        nx.draw(G, pos, with_labels=True, node_size=7000, node_color='pink',  font_size=11, font_weight='bold', arrowsize=30)  # Dibujar el grafo con etiquetas de nodos, tamaño y estilo de nodo personalizados
        labels = nx.get_edge_attributes(G, 'weight')  # Obtener los atributos de peso de las aristas
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)  # Dibujar las etiquetas de las aristas
        plt.title("Grafo del Sistema de Transporte")  # Establecer el título del gráfico
        plt.show()  # Mostrar el gráfico

# Crear un sistema de transporte
sistema = Transportesdelllano()

# Agregar conexiones entre estaciones y tiempos de viaje
sistema.agregar_conexion("Sanjose", "Versalles", 15)
sistema.agregar_conexion("Sanjose", "Centro", 20)
sistema.agregar_conexion("Versalles", "Alcaravanes", 10)
sistema.agregar_conexion("Centro", "Alcaravanes", 8)
sistema.agregar_conexion("Centro", "Olimpico", 10)
sistema.agregar_conexion("Alcaravanes", "Olimpico", 5)
sistema.agregar_conexion("Alcaravanes", "Pradera", 15)
sistema.agregar_conexion("Olimpico", "Pradera", 7)
