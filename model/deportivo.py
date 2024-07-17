from model.deportivo import vehiculo

class deportivo(vehiculo):
   
    def __init__(self,marca,modelo,anio,velocidad_max):
        super()._init_(marca,modelo,anio)
        self.velocidad_max=velocidad_max
    
    def descripcion(self):
        return f"{super().descripcion()},velicidad: {self.velocidad_max}"
        