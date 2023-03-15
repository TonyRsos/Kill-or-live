class Personaje:
    
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
        
        
class Enemigo(Personaje):
    
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, poder_enemigo, tipo_enemigo):
        self.poder_enemigo = poder_enemigo
        self.tipo_enemigo = tipo_enemigo
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        
class Protagonista(Personaje):
    
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, poder_protagonista):
        self.poder_protagonista = poder_protagonista
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        
poder_posible = ['Fuego', 'Aire', 'Agua', 'Rayo', 'Tierra', 'Oscuridad']
enemigos_posibles = ['Enano', 'Gigante', 'Mago']