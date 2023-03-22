from dataclasses import dataclass

@dataclass
class Caracteristicas:
    poder_posible = ['Fuego', 'Aire', 'Agua', 'Rayo', 'Tierra', 'Oscuridad']
    
    nombre: str
    tipo_de_poder: str
    tipo_enemigo = str
    fuerza: int = 0
    inteligencia: int = 0
    defensa: int = 0
    vida: int = 0
    
    def validar_tipo_de_poder(self, tipo_de_poder):
        if tipo_de_poder in self.poder_posible:
            return tipo_de_poder
        else:
            return self.poder_posible[0]
        


class Personaje:
    def __init__(self, caracteristicas):
        self.nombre = caracteristicas.nombre
        self.fuerza = caracteristicas.fuerza
        self.inteligencia = caracteristicas.inteligencia
        self.defensa = caracteristicas.defensa
        self.vida = caracteristicas.vida
        self.tipo_de_poder = caracteristicas.validar_tipo_de_poder(caracteristicas.tipo_de_poder)
        self.tipo_enemigo = caracteristicas.validar_tipo_enemigo(caracteristicas.tipo_enemigo)
        
        
class Enemigo(Personaje):
    enemigo_posible = ['Enano', 'Gigante', 'Mago']
    def __init__(self, caracteristicas):
        super().__init__(caracteristicas)
         
    def validar_tipo_enemigo(self, tipo_enemigo):
        if tipo_enemigo in self.enemigo_posible:
            return tipo_enemigo
        else:
            return self.enemigo_posible[0]
class Protagonista(Personaje):
    def __init__(self, caracteristicas):
        super().__init__(caracteristicas)