from random import randrange

def najdi_pozice(pole, hledany):
    seznam = []
    for cislo, znak in enumerate(pole):
        if znak == hledany:
            seznam.append(cislo)	
    return seznam

def tah_pocitace(pole):
    "Vrátí herní pole se zaznamenaným tahem počítače"
    seznam = najdi_pozice(pole, 'x')
    for cislo_policka in seznam:
        if  (cislo_policka == 0) and (pole[cislo_policka + 1] == '-'):
            return tah(pole, cislo_policka + 1, 'o')
        elif (cislo_policka == 19) and (pole[cislo_policka - 1] == '-'):
            return tah(pole, cislo_policka - 1, 'o')
        elif (cislo_policka > 0) and (cislo_policka < 19):
            if (pole[cislo_policka + 1] == '-'):
                return tah(pole, cislo_policka + 1, 'o')
            elif (pole[cislo_policka - 1] == '-'):
                return tah(pole, cislo_policka - 1, 'o')

    while True:
        cislo_policka = randrange(20)
        if '-' in pole[cislo_policka]:
            return tah(pole, cislo_policka, 'o')