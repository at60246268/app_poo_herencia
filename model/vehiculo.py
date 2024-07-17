class vehiuculo:
    def __init__(self, marca, modelo, anio):
        self.marca=marca
        self.modelo=modelo
        self.anio=anio
    
    def descripcio(self):
        return f"{self.marca},{self.modelo},{self.anio}"
    
    def tipo(self):
        return "veiculo generico"