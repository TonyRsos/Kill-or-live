class Personaje:
    
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, tipo_de_poder):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
        self.tipo_de_poder = tipo_de_poder
        
class Enemigo(Personaje):
    
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, tipo_de_poder, tipo_enemigo):
        self.tipo_enemigo = tipo_enemigo
        super().__init__(nombre, fuerza, inteligencia, defensa, vida, tipo_de_poder)
        
class Protagonista(Personaje):
    
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, tipo_de_poder):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida, tipo_de_poder)
        
poder_posible = ['Fuego', 'Aire', 'Agua', 'Rayo', 'Tierra', 'Oscuridad']
enemigos_posibles = ['Enano', 'Gigante', 'Mago']
