def konwertuj_na_rzymska(liczba_arabska):
    jednosci = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
    dziesiatki = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    setki = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    tysiace = ['', 'M', 'MM', 'MMM']

    arab = str(liczba_arabska).zfill(4)    #służy do wypełnienia liczby arabskiej zerami z przodu, aby miała zawsze długość 4 znaków

    wynik = (
            tysiace[int(arab[-4])] +
            setki[int(arab[-3])] +
            dziesiatki[int(arab[-2])] +
            jednosci[int(arab[-1])]
    )

    return wynik


class LiczbaRzymska:
    def __init__(self, liczba_arabska):
        self.liczba_arabska = int(liczba_arabska)
        self.liczba_rzymska = konwertuj_na_rzymska(self.liczba_arabska)

    def __str__(self):
        return self.liczba_rzymska

    def __int__(self):
        return self.liczba_arabska

    def __eq__(self, other):
        if isinstance(other, LiczbaRzymska):
            return self.liczba_arabska == other.liczba_arabska
        return False

    def __lt__(self, other):
        if isinstance(other, LiczbaRzymska):
            return self.liczba_arabska < other.liczba_arabska
        return False

    def __add__(self, other):
        if isinstance(other, LiczbaRzymska):
            return LiczbaRzymska(self.liczba_arabska + other.liczba_arabska)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, LiczbaRzymska):
            self.liczba_arabska += other.liczba_arabska
            self.liczba_rzymska = konwertuj_na_rzymska(self.liczba_arabska)
            return self
        return NotImplemented

    def __len__(self):
        return len(self.liczba_rzymska)

    def __mul__(self, other):
        if isinstance(other, LiczbaRzymska):
            return LiczbaRzymska(self.liczba_arabska * other.liczba_arabska)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, LiczbaRzymska):
            wynik = self.liczba_arabska - other.liczba_arabska
            if wynik <= 0:
                raise ValueError('Wynik jest liczbą mniejszą od zera')
            return LiczbaRzymska(wynik)
        return NotImplemented


# Przykłady użycia
a = LiczbaRzymska(150)
b = LiczbaRzymska(2395)

print(a)  # CL (150)
print(int(a))  # 150
print(a == b, a < b, a > b)  # False, True, False
print(a + b)  # MMDXLV (2545)
print('V' in str(a), 'X' in str(a), 'L' in str(a))  # False, False, True
a += b  # _iadd_
print(a, b)  # MMDXLV(2545) MMCCCXCV (2395)
print(len(a))  # 6

c = LiczbaRzymska(3)
d = LiczbaRzymska(8)

print(c * d)  # XXIV (24)
print(d - c)  # V (5)
try:
    print(c - d)  # ValueError: Wynik jest liczbą mniejszą od zera
except ValueError as e:
    print(e)
