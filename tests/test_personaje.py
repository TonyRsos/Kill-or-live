from killOrLive import Personaje, Enemigo, Caracteristicas, Protagonista

PODER_NO_PERMITIDO = 'Luz'
ENEMIGO_NO_POSIBLE = 'bruja'

caracteristicas = Caracteristicas('andres',PODER_NO_PERMITIDO)
enemigo_caracteristicas = Caracteristicas('andres', 'Fuego', 10, 10, 10, 10)
enemigo = Enemigo(ENEMIGO_NO_POSIBLE, enemigo_caracteristicas)

def test_poder_posible_personaje():
    personaje = Protagonista(caracteristicas)
    assert personaje.tipo_de_poder != PODER_NO_PERMITIDO
    
def test_enemigo_posible_personaje():
    enemigo = Enemigo(ENEMIGO_NO_POSIBLE, enemigo_caracteristicas)
    assert enemigo.tipo_enemigo != ENEMIGO_NO_POSIBLE