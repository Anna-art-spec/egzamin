import random

class Gra:
    def __init__(self, num=None):
        self._num = num if num is not None else random.randint(1, 10)
        self._aktualna_proba = 1
        self._odgadnieto = False

    def koniec_gry(self):
        return self._aktualna_proba > 5 or self._odgadnieto

    def wygrana(self):
        return self._odgadnieto

    def zgadnij(self, liczba):
        if self.koniec_gry():
            print('Gra zakończona.')
            return
        if not isinstance(liczba, int) or liczba < 1 or liczba > 10:
            print('Wybrana opcja nie jest cyfrą od 1 do 10')
            return
        print(f'Próba nr {self._aktualna_proba}')
        self._aktualna_proba += 1
        if liczba == self._num:
            self._odgadnieto = True
            print('Gratulacje! Odgadłeś liczbę.')
        else:
            print('Nieudana próba')
            if self.koniec_gry() and not self._odgadnieto:
                print('Niestety, nie udało się. Koniec gry.')

def main():
    gra = Gra()
    while not gra.koniec_gry():
        try:
            liczba = int(input('Podaj liczbę od 1 do 10: '))
        except ValueError:
            print('Wybrana opcja nie jest cyfrą od 1 do 10')
            continue
        gra.zgadnij(liczba)
    if gra.wygrana():
        print('Gratulacje! Odgadłeś liczbę.')
    else:
        print('Niestety, nie udało się. Koniec gry.')

if __name__ == '__main__':
    main()
