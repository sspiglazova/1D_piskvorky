import ai #tah_pocitace
import util #tah

def vyhodnot(pole):
    if 'xxx' in pole:
        return 'x', pole
    elif 'ooo' in pole:
        return 'o', pole
    elif '-' not in pole:
        return '!', pole
    else:
        return '-'

def tah_hrace(pole, cislo_policka):
    while True:
        if (cislo_policka >= 0) and (cislo_policka <= 19) and (pole[cislo_policka] == '-'):
            return util.tah(pole, cislo_policka, 'x')
        else:
            print('bud pole je obsazeno nebo cislo je zaporne nebo prilis velke')

def zadej_cislo_policka(otazka):
    while True:
        try:
            cislo_policka = int(input(otazka))
            if cislo_policka < 0:
                raise ArithmeticError('cislo je zaporne')
            return cislo_policka
        except ValueError:
            print('to neni cislo')
        except ArithmeticError:
            print('cislo je zaporne')

def piskvorky1d(pole):
    while '-' in pole:
        print(pole)
        cislo_policka = zadej_cislo_policka('Zadej cislo_policka: ')
        pole = tah_hrace(pole, cislo_policka)
        pole = ai.tah_pocitace(pole)
        result = vyhodnot(pole)
        if result != '-':
            print(result)
            break
