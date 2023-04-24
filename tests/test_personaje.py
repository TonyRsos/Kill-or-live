from killOrLive import Enemigo, Caracteristicas, Protagonista

PODER_NO_PERMITIDO = 'Luz'
ENEMIGO_NO_POSIBLE = 'bruja'


def test_poder_posible_personaje():
    caracteristicas = Caracteristicas('andres',PODER_NO_PERMITIDO)
    personaje = Protagonista(caracteristicas)
    assert personaje.tipo_de_poder != PODER_NO_PERMITIDO
    
def test_enemigo_posible_personaje():
    enemigo = Enemigo(ENEMIGO_NO_POSIBLE)
    assert enemigo.tipo_enemigo != ENEMIGO_NO_POSIBLE
    
def test_putazo_que_cura():
    caracteristicas = Caracteristicas('andres',Caracteristicas.poder_posible[0])
    enemigo = Enemigo()
    personaje = Protagonista(caracteristicas)
    vida_anterior = personaje.vida
    personaje.defensa = 200
    enemigo.fuerza = 100
    enemigo.atacar(personaje)
    assert vida_anterior >= personaje.vida
    
    