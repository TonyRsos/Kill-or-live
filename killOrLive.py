from dataclasses import dataclass

@dataclass
class Caracteristicas:
    poder_posible = ['Fuego', 'Aire', 'Agua', 'Rayo', 'Tierra', 'Oscuridad']
    
    nombre: str
    tipo_de_poder: str
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
        
    def __repr__(self):
        representation = f"""
        Nombre: {self.nombre}
        Fuerza: {self.fuerza}
        Inteligencia: {self.inteligencia}
        Defensa: {self.defensa}
        Vida: {self.vida}
        Tipo de poder: {self.tipo_de_poder}
        """
        return representation
        
        
class Enemigo(Personaje):
    enemigo_posible = {
        'Enano': {'nombre':'Hassbulla', 'fuerza':100, 'inteligencia':100, 'defensa':100, 'vida':100, 'tipo_de_poder': 'Fuego'},
        'Mago': {'nombre':'El mago miado', 'fuerza':1000, 'inteligencia':50, 'defensa':100, 'vida':100, 'tipo_de_poder': 'Aire'},
        'Gigante': {'nombre':'Big Show', 'fuerza':1500, 'inteligencia':50, 'defensa':50, 'vida':100, 'tipo_de_poder': 'Oscuridad'}
    }
    
    def __init__(self,tipo_enemigo):
        self.tipo_enemigo = self.validar_tipo_enemigo(tipo_enemigo)
        super().__init__(Caracteristicas(**Enemigo.enemigo_posible[tipo_enemigo]))
         
    def validar_tipo_enemigo(self, tipo_enemigo):
        if tipo_enemigo in self.enemigo_posible:
            return tipo_enemigo
        else:
            return self.enemigo_posible[0]

class Protagonista(Personaje):
    def __init__(self, caracteristicas):
        super().__init__(caracteristicas)
        
enemigo1 = Enemigo('Gigante')
print(enemigo1)