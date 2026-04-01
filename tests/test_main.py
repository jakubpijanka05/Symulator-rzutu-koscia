import pytest
from app.main import rzut_koscia, oblicz_statystyki, symulacja_masowa, tryb_gry

def test_rzut_koscia_zakres():
    wynik_k6 = rzut_koscia(6)
    assert 1 <= wynik_k6 <= 6
    wynik_k20 = rzut_koscia(20)
    assert 1 <= wynik_k20 <= 20

def test_rzut_koscia_nieprawidlowa():
    with pytest.raises(ValueError):
        rzut_koscia(10)

def test_oblicz_statystyki():
    wyniki = [2, 4, 6, 8]
    stats = oblicz_statystyki(wyniki)
    assert stats["suma"] == 20
    assert stats["srednia"] == 5.0
    assert stats["min"] == 2
    assert stats["max"] == 8

def test_oblicz_statystyki_pusta_lista():
    stats = oblicz_statystyki([])
    assert stats["suma"] == 0

def test_symulacja_masowa():
    wyniki = symulacja_masowa(4, 50)
    assert len(wyniki) == 50
    assert all(1 <= w <= 4 for w in wyniki)

def test_symulacja_masowa_zla_liczba():
    with pytest.raises(ValueError):
        symulacja_masowa(6, 0)

def test_tryb_gry():
    wynik_gry = tryb_gry(6, 15)
    assert wynik_gry["koncowa_suma"] >= 15
    assert len(wynik_gry["historia_rzutow"]) == wynik_gry["liczba_rund"]
