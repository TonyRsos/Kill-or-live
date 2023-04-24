from dataclasses import dataclass
from random import randrange

@dataclass
class Caracteristicas:
    poder_posible = ['Fuego', 'Aire', 'Agua', 'Rayo', 'Tierra', 'Oscuridad']
    
    nombre: str
    tipo_de_poder: str
    fuerza: int = 100
    inteligencia: int = 100
    defensa: int = 100
    vida: int = 100
    recistencia = 100
    suerte = 100
    
    def validar_tipo_de_poder(self, tipo_de_poder):
        if tipo_de_poder in self.poder_posible:
            return tipo_de_poder
        else:
            return self.poder_posible[0]
        
    def mostrar_menu():
        pass
        
class Personaje:
    def __init__(self, caracteristicas: Caracteristicas):
        self.nombre = caracteristicas.nombre
        self.fuerza = caracteristicas.fuerza
        self.inteligencia = caracteristicas.inteligencia
        self.defensa = caracteristicas.defensa
        self.vida = caracteristicas.vida
        self.tipo_de_poder = caracteristicas.validar_tipo_de_poder(caracteristicas.tipo_de_poder)
        self.recistencia = caracteristicas.recistencia
        self.suerte = caracteristicas.suerte

        print("Atributos base")

    def atributos(self):   #Se crea un metodo donde muestra el valor de sus atributos
        
        print(self.nombre, ":", sep="")
        print("·Fuerza:", self.fuerza)
        print("·Inteligencia:", self.inteligencia)
        print("·Defensa:", self.defensa)
        print("·Vida:", self.vida)
        print(".Recistencia:", self.recistencia)
        print(".Suerte:", self.suerte)
    
    def level_up(self, fuerza, inteligencia, defensa, recistencia, suerte): #En este metodo nos indica el aumento en las estadisticas al subir de nivel el jugador
        print("***Nuevas estadisticas de nivel***")
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa
        self.recistencia = self.recistencia + recistencia
        self.suerte = self.suerte + suerte + randrange(5, 27, 4) #Al agregar este atributo de suerte sera sumado a la base mas el random
    
    def death_live(self): #En este metodo se indica si el jugador esta vivo o muerto
        print("*************")
        print("El personaje esta:..")
        if self.vida <= 0:
            print("muerto")
        elif self.vida > 0:
            print("VIVO")
        return self.vida > 0
    
    def daño(self,enemigo): #Metodo donde se implemente el daño al enemigo
        print("***Daño***")
        return self.fuerza - enemigo.defensa
    
    def atacar(self, enemigo: 'Personaje'): #metodo donde muestra el daño de ataque hacia el enemigo
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "ha realizado", daño, " puntos de daño a ", enemigo.nombre)
        if enemigo.death_live():
            print("vida de ", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()
        print("La vida del enemigo es: ", enemigo.vida)
        print("****Nuevas estadisticas del enemigo:*****")

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
        
enemigo1 = Enemigo('Enano')
print(enemigo1)

caracteristicas = Caracteristicas('Jesus', 'Agua')
mi_personaje = Personaje(caracteristicas)
mi_personaje.level_up(1,2,0,3,5)
mi_personaje.atributos()
print(mi_personaje.death_live())
print(mi_personaje.daño(enemigo1))
mi_personaje.atacar(enemigo1)
enemigo1.atributos()