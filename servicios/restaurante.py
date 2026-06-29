from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    def __init__(self, nombre_restaurante: str):
        self.nombre_restaurante: str = nombre_restaurante
        self.lista_productos: list[Producto] = []
        self.lista_clientes: list[Cliente] = []

    def agregar_producto(self, producto: Producto) -> None:
        self.lista_productos.append(producto)

    def registrar_cliente(self, cliente: Cliente) -> None:
        self.lista_clientes.append(cliente)

    def mostrar_informacion(self) -> None:
        print(f"\n=== SISTEMA DE GESTIÓN: {self.nombre_restaurante.upper()} ===")
        
        print("\n--- MENÚ DE PRODUCTOS ---")
        for prod in self.lista_productos:
            print(prod)
            
        print("\n--- CLIENTES REGISTRADOS ---")
        for cli in self.lista_clientes:
            print(cli)