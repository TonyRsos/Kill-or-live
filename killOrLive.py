class Personaje:
    
    poder_posible = ['Fuego', 'Aire', 'Agua', 'Rayo', 'Tierra', 'Oscuridad']
    
    def __init__(self, nombre, tipo_de_poder, fuerza=0, inteligencia=0, defensa=0, vida=0):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
        self.tipo_de_poder = self.validar_tipo_de_poder(tipo_de_poder) 
        
    def validar_tipo_de_poder(self, tipo_de_poder):
        if tipo_de_poder in self.poder_posible:
            return tipo_de_poder
        else:
            return self.poder_posible[0]
        
class Enemigo(Personaje):
    
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, tipo_de_poder, tipo_enemigo):
        self.tipo_enemigo = tipo_enemigo
        super().__init__(nombre, fuerza, inteligencia, defensa, vida, tipo_de_poder)
        
class Protagonista(Personaje):
    
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, tipo_de_poder):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida, tipo_de_poder)
        
enemigos_posibles = ['Enano', 'Gigante', 'Mago']
