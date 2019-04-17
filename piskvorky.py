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

def piskvorky1d(pole):
        cislo_policka = 0
        while '-' in pole:
            print(pole)
            print('zadej cislo policky od 0 do {}'. format(len(pole)-1))
            # kontrola cislo_policka pro uzivatele
            while True:
                try:
                    cislo_policka = int(input())
                    if cislo_policka < 0:
                        raise ArithmeticError('cislo je zaporne')
                except ValueError:
                    print('to neni cislo')
                except ArithmeticError:
                    print('cislo je zaporne')

            pole = tah_hrace(pole, cislo_policka)
            pole = ai.tah_pocitace(pole)
            result = vyhodnot(pole)
            if result != '-':
                print(result)
                break