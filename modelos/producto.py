# modelos/producto.py

class Producto:
    def __init__(self, nombre: str, precio: float, stock: int, disponible: bool):
        # Asegúrate de que diga self.nombre exactamente así
        self.nombre: str = nombre
        self.precio: float = precio
        self.stock: int = stock
        self.disponible: bool = disponible

    def __str__(self) -> str:
        estado = "Disponible" if self.disponible else "Agotado"
        return f"Producto: {self.nombre} | Precio: ${self.precio:.2f} | Stock: {self.stock} u. ({estado})"