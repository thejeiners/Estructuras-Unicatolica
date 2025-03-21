import time

class RouteNode:
    def __init__(self, location):
        self.location = location
        self.next = None

class Route:
    def __init__(self):
        self.head = None

    def add_location(self, location):
        new_node = RouteNode(location)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def show_route(self):
        current = self.head
        if not current:
            print(" No hay una ruta definida.")
            return
        print(" Ruta definida:")
        while current is not None:
            print(f" {current.location}")
            current = current.next

    def navigate_route(self):
        current = self.head
        if not current:
            print(" No hay una ruta para navegar.")
            return

        print(" Iniciando recorrido...")

        while current:
            time.sleep(1.5)
            print(f"Llegaste a: {current.location}")
            current = current.next

        print(" Fin del recorrido.")

locations = [
    "Avenida Central",
    "Calle 5",
    "Plaza Mayor",
    "Avenida del Río",
    "Estación Norte",
    "Parque Sur",
    "Museo Nacional",
    "Teatro Municipal",
    "Universidad Central",
    "Biblioteca Pública"
]

if __name__ == "__main__":
    city_route = Route()
    codigo = input("Ingrese su código: ")

    if int(codigo[-1]) % 2 == 0:  # Último dígito par
        print(" Ruta con ubicaciones en índices pares:")
        for i in range(0, len(locations), 2):
            city_route.add_location(locations[i])
    else:  # Último dígito impar
        print(" Ruta con ubicaciones en índices impares:")
        for i in range(1, len(locations), 2):
            city_route.add_location(locations[i])

    city_route.show_route()

    print("\n Simulación del recorrido en la ruta:\n")
    city_route.navigate_route()
