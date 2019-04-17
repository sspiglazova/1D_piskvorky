import piskvorky, ai, util, pytest

# test funkce vyhodnot
def test_vyhodnot_x():
    assert piskvorky.vyhodnot("----xxx-------------") == ('x', "----xxx-------------")

def test_vyhodnot_o():
    assert piskvorky.vyhodnot("----ooo-------------") == ('o', "----ooo-------------")

def test_vyhodnot_remiza():
    assert piskvorky.vyhodnot("oxoxoxoxoxoxoxoxoxox") == ('!', "oxoxoxoxoxoxoxoxoxox")

def test_vyhodnot_pokracuj():
    assert piskvorky.vyhodnot("--------------------") == ('-')

# test funkve najdi_pozice
def test_najdi_pozice():
    assert ai.najdi_pozice('-xox----oxo-------x-', 'x') == [1, 3, 9, 18]

# test funkce tah_pocitace
def test_tah_pocitace():
    seznam = [1, 3, 9, 18]
    assert ai.tah_pocitace('-xox----oxo-------x-') == ('oxox----oxo-------x-')

# test  funkce tah
def test_tah_x():
    assert util.tah ('-xox----oxo-------x-', 19, 'x') == '-xox----oxo-------xx'

def test_tah_o():
    assert util.tah ('-xox----oxo-------x-', 0, 'o') == 'oxox----oxo-------x-'