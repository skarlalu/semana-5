class Cliente:
    def __init__(self, cedula: str, nombre: str, edad: int, es_vip: bool):
        self.cedula: str = cedula
        self.nombre: str = nombre
        self.edad: int = edad
        self.es_vip: bool = es_vip

    def __str__(self) -> str:
        tipo_cliente = "VIP" if self.es_vip else "Regular"
        return f"Cliente: {self.nombre} (C.I.: {self.cedula}) | Edad: {self.edad} | Tipo: {tipo_cliente}"