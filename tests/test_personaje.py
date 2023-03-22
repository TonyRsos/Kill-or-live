from killOrLive import Personaje, Enemigo, Caracteristicas, Protagonista

PODER_NO_PERMITIDO = 'Luz'
ENEMIGO_NO_POSIBLE = 'bruja'

caracteristicas = Caracteristicas('andres',PODER_NO_PERMITIDO, ENEMIGO_NO_POSIBLE)

def test_poder_posible_personaje():
    personaje = Protagonista(caracteristicas)
    assert personaje.tipo_de_poder != PODER_NO_PERMITIDO
    
#def test_enemigo_posible_personaje():
    #enemigo = Enemigo(enemigo)
    #assert enemigo.tipo_enemigo != ENEMIGO_NO_POSIBLE