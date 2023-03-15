class Personaje:
    
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
        
        
class Enemigo(Personaje):
    
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)