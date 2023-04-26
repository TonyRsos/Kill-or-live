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
    vida: int = 1000
    recistencia: int = 100
    suerte: int = 100
    
    def validar_tipo_de_poder(self, tipo_de_poder):
        if tipo_de_poder in self.poder_posible:
            return tipo_de_poder
        else:
            return self.poder_posible[0]

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
    
    def daño(self, enemigo: 'Personaje'): #Metodo donde se implemente el daño al enemigo
        print("***Daño***")
        dano = self.fuerza - enemigo.defensa
        if dano > 0:
            return dano
        else:
            return 0
    
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
        'Enano': {'nombre':'Hassbulla', 'fuerza':200, 'inteligencia':100, 'defensa':100, 'vida':1000, 'tipo_de_poder': 'Fuego'},
        'Mago': {'nombre':'El mago miado', 'fuerza':150, 'inteligencia':50, 'defensa':100, 'vida':1000, 'tipo_de_poder': 'Aire'},
        'Gigante': {'nombre':'Big Show', 'fuerza':200, 'inteligencia':50, 'defensa':50, 'vida':1000, 'tipo_de_poder': 'Oscuridad'}
    }
    
    def __init__(self, tipo_enemigo = 'Enano'):
        self.tipo_enemigo = self.validar_tipo_enemigo(tipo_enemigo)
        super().__init__(Caracteristicas(**Enemigo.enemigo_posible[self.tipo_enemigo]))
         
    def validar_tipo_enemigo(self, tipo_enemigo):
        if tipo_enemigo in self.enemigo_posible:
            return tipo_enemigo
        else:
            return list(self.enemigo_posible.keys())[0]
        

class Protagonista(Personaje):
    def __init__(self, caracteristicas):
        super().__init__(caracteristicas)

class Protagonista(Personaje):
    def _init_(self, caracteristicas):
        super()._init_(caracteristicas)

def seleccionar_poder():
    print("Selecciona el tipo de poder que deseas:")
    for idx, poder in enumerate(Caracteristicas.poder_posible):
        print(f"{idx + 1}. {poder}")
    opcion = int(input())
    return Caracteristicas.poder_posible[opcion - 1]


def seleccionar_enemigo():
    print("Selecciona el enemigo con el que deseas pelear:")
    for idx, enemigo in enumerate(Enemigo.enemigo_posible):
        print(f"{idx + 1}. {enemigo}")
    opcion = int(input())
    enemigo_key = list(Enemigo.enemigo_posible.keys())[opcion - 1]
    return enemigo_key


def menu_combate(protagonista: Protagonista, enemigo: Enemigo):
    while protagonista.death_live() and enemigo.death_live():
        print("\nAcciones:")
        print("1. Atacar al enemigo")
        print("2. Defender y contraatacar (recibir la mitad del daño y devolverlo al enemigo)")
        print("3. Rendirse")

        opcion = int(input())

        if opcion == 1:
            protagonista.atacar(enemigo)
            enemigo.atacar(protagonista)
        elif opcion == 2:
            daño_enemigo = enemigo.daño(protagonista) // 2
            protagonista.vida -= daño_enemigo
            enemigo.vida -= daño_enemigo
            print(f"{protagonista.nombre} ha defendido y contraatacado, causando {daño_enemigo} puntos de daño a {enemigo.nombre}")
        elif opcion == 3:
            print(f"{protagonista.nombre} se ha rendido.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

    if protagonista.vida <= 0:
        print(f"{protagonista.nombre} ha perdido la batalla.")
    elif enemigo.vida <= 0:
        print(f"{protagonista.nombre} ha derrotado a {enemigo.nombre}.")


def main():
    nombre = input("Ingresa el nombre de tu personaje: ")
    poder = seleccionar_poder()
    caracteristicas = Caracteristicas(nombre=nombre, tipo_de_poder=poder)
    protagonista = Protagonista(caracteristicas)

    tipo_enemigo = seleccionar_enemigo()
    enemigo = Enemigo(tipo_enemigo)

    menu_combate(protagonista, enemigo)

if __name__ == "__main__":
    main()