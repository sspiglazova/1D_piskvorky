import piskvorky
import ai

def test_tah_na_prazdne_pole():
    pole = ai.tah_pocitace('--------------------')
    assert len(pole) == 20
    assert pole.count('x') == 1
    assert pole.count('-') == 19