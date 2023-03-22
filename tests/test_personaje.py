PODER_NO_PERMITIDO = 'Luz'

from killOrLive import Personaje

def test_poder_posible_personaje():
    personaje = Personaje('', PODER_NO_PERMITIDO)
    assert personaje.tipo_de_poder != PODER_NO_PERMITIDO