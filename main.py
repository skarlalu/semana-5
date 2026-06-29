import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.cliente import Cliente

def iniciar_programa():
    mi_restaurante = Restaurante("El Buen Sabor")

    producto1 = Producto("Hamburguesa Artesanal", 8.50, 20, True)
    producto2 = Producto("Jugo Natural de Naranja", 2.25, 15, True)
    
    cliente1 = Cliente("0987654321", "Kevin Morocho", 24, True)
    cliente2 = Cliente("0912345678", "María Flores", 30, False)

    mi_restaurante.agregar_producto(producto1)
    mi_restaurante.agregar_producto(producto2)
    
    mi_restaurante.registrar_cliente(cliente1)
    mi_restaurante.registrar_cliente(cliente2)

    mi_restaurante.mostrar_informacion()

if __name__ == "__main__":
    iniciar_programa()