import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from gra import Gra, main

class TestGra(unittest.TestCase):

    def test_przekroczono_ilosc_prob(self):
        gra = Gra()
        gra._aktualna_proba = 6
        self.assertTrue(gra.koniec_gry())

    def test_sprobuj_zgadnac_gdy_gra_skonczona(self):
        gra = Gra()
        gra._aktualna_proba = 6
        with patch('builtins.print') as mocked_print:
            gra.zgadnij(5)
            mocked_print.assert_called_with('Gra zakończona.')

    def test_odgadnieto_liczbe_w_pierwszej_probie(self):
        gra = Gra()
        gra._num = 7
        with patch('builtins.print') as mocked_print:
            gra.zgadnij(7)
            self.assertTrue(gra.wygrana())
            mocked_print.assert_any_call('Gratulacje! Odgadłeś liczbę.')

    def test_nie_odgadnieto_liczby(self):
        gra = Gra()
        gra._num = 7
        with patch('builtins.print') as mocked_print:
            gra.zgadnij(5)
            self.assertFalse(gra.wygrana())
            mocked_print.assert_any_call('Próba nr 1')
            mocked_print.assert_any_call('Nieudana próba')

    def test_utworzono_gre_bez_prob_zgadywania(self):
        gra = Gra()
        self.assertFalse(gra.wygrana())
        self.assertEqual(gra._aktualna_proba, 1)

    def test_odgadnieto_liczbe_w_ostatniej_probie(self):
        gra = Gra()
        gra._aktualna_proba = 5
        gra._num = 7
        with patch('builtins.print') as mocked_print:
            gra.zgadnij(7)
            self.assertTrue(gra.wygrana())
            mocked_print.assert_any_call('Gratulacje! Odgadłeś liczbę.')

    def test_komunikaty_wyswietlane_w_grze(self):
        gra = Gra()
        gra._num = 7
        with patch('builtins.print') as mocked_print:
            gra.zgadnij(5)
            mocked_print.assert_any_call('Próba nr 1')
            mocked_print.assert_any_call('Nieudana próba')
            gra.zgadnij(7)
            mocked_print.assert_any_call('Próba nr 2')
            mocked_print.assert_any_call('Gratulacje! Odgadłeś liczbę.')

    def test_walidacja_wejscia(self):
        gra = Gra()
        with patch('builtins.print') as mocked_print:
            gra.zgadnij('a')
            mocked_print.assert_called_with('Wybrana opcja nie jest cyfrą od 1 do 10')
            gra.zgadnij(0)
            mocked_print.assert_called_with('Wybrana opcja nie jest cyfrą od 1 do 10')
            gra.zgadnij(11)
            mocked_print.assert_called_with('Wybrana opcja nie jest cyfrą od 1 do 10')

    @patch('builtins.input', side_effect=[1, 2, 3, 4, 6, StopIteration])
    @patch('gra.random.randint', return_value=5)
    def test_interaktywna_gra_nieudana(self, mock_randint, mock_input):
        with patch('builtins.print') as mocked_print:
            main()
            mocked_print.assert_any_call('Próba nr 1')
            mocked_print.assert_any_call('Nieudana próba')
            mocked_print.assert_any_call('Próba nr 2')
            mocked_print.assert_any_call('Nieudana próba')
            mocked_print.assert_any_call('Próba nr 3')
            mocked_print.assert_any_call('Nieudana próba')
            mocked_print.assert_any_call('Próba nr 4')
            mocked_print.assert_any_call('Nieudana próba')
            mocked_print.assert_any_call('Próba nr 5')
            mocked_print.assert_any_call('Niestety, nie udało się. Koniec gry.')

    @patch('builtins.input', side_effect=[1, 2, 3, 4, 5, StopIteration])
    @patch('gra.random.randint', return_value=5)
    def test_interaktywna_gra_udana(self, mock_randint, mock_input):
        with patch('builtins.print') as mocked_print:
            main()
            mocked_print.assert_any_call('Próba nr 1')
            mocked_print.assert_any_call('Nieudana próba')
            mocked_print.assert_any_call('Próba nr 2')
            mocked_print.assert_any_call('Nieudana próba')
            mocked_print.assert_any_call('Próba nr 3')
            mocked_print.assert_any_call('Nieudana próba')
            mocked_print.assert_any_call('Próba nr 4')
            mocked_print.assert_any_call('Nieudana próba')
            mocked_print.assert_any_call('Próba nr 5')
            mocked_print.assert_any_call('Gratulacje! Odgadłeś liczbę.')


@patch('builtins.input', side_effect=['a', '0', '11', '5'])
@patch('sys.stdout', new_callable=StringIO)
@patch('gra.random.randint', return_value=5)
def test_interaktywna_gra_nieprawidlowe_wejscie(self, mock_randint, mock_stdout, mock_input):
    main()
    captured_output = mock_stdout.getvalue()
    self.assertIn('Wybrana opcja nie jest cyfrą od 1 do 10', captured_output)

@patch('builtins.input', side_effect=['a', '0', '11', '5'])
@patch('sys.stdout', new_callable=StringIO)
def test_main_nieprawidlowe_wejscia(self, mock_stdout, mock_input):
    with self.assertRaises(ValueError):
        main()
    captured_output = mock_stdout.getvalue()
    expected_output = 'Wybrana opcja nie jest cyfrą od 1 do 10\n' * 3
    self.assertEqual(captured_output, expected_output)







if __name__ == '__main__':
    unittest.main()



