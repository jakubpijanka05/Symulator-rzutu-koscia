import random


    """Symuluje rzut pojedynczą kością. Obsługuje format 'K6' oraz liczbę 6."""
    if isinstance(typ_kosci, str):
        if typ_kosci.upper().startswith('K'):
            sciany = int(typ_kosci[1:])
        else:
            sciany = int(typ_kosci)
    else:
        sciany = int(typ_kosci)

    if sciany not in [4, 6, 20]:
        raise ValueError("Nieobsługiwany typ kości")

    return random.randint(1, sciany)

def oblicz_statystyki(wyniki):
    """Oblicza podstawowe statystyki z listy rzutów."""
    if not wyniki:
        return {"suma": 0, "srednia": 0, "min": 0, "max": 0}
    return {
        "suma": sum(wyniki),
        "srednia": sum(wyniki) / len(wyniki),
        "min": min(wyniki),
        "max": max(wyniki)
    }

def symulacja_masowa(typ_kosci, liczba_rzutow):
    """Przeprowadza masową symulację rzutów."""
    if liczba_rzutow <= 0:
        raise ValueError("Liczba rzutów musi być większa od zera")
    return [rzut_koscia(typ_kosci) for _ in range(liczba_rzutow)]

def tryb_gry(typ_kosci, prog_zwyciestwa):
    """Tryb gry: rzuca aż do osiągnięcia progu punktowego."""
    historia_rzutow = []
    suma_punktow = 0
    while suma_punktow < prog_zwyciestwa:
        wynik = rzut_koscia(typ_kosci)
        historia_rzutow.append(wynik)
        suma_punktow += wynik
    return {
        "liczba_rund": len(historia_rzutow),
        "historia_rzutow": historia_rzutow,
        "koncowa_suma": suma_punktow
    }

def interaktywne_menu():
    """Główny interfejs użytkownika w konsoli."""
    print("\n" + "="*40)
    print(" PROFESJONALNY SYMULATOR KOŚCI RPG ")
    print("="*40)
    
    while True:
        print("\nWYBIERZ TRYB:")
        print("[1] Pojedynczy rzut")
        print("[2] Tryb Gry (rzuty aż do progu)")
        print("[3] Symulacja masowa + Statystyki")
        print("[0] Wyjście")
        
        opcja = input("\nTwój wybór: ").strip()

        if opcja == '0':
            print("Zamykanie... Do zobaczenia!")
            break

        if opcja in ['1', '2', '3']:
            kosc = input("Wybierz kość (4, 6 lub 20): ").strip()
            if kosc not in ['4', '6', '20']:
                print("BŁĄD: Wybierz 4, 6 lub 20.")
                continue
            
            kod_kosci = f"K{kosc}"

            if opcja == '1':
                print(f"\n>>> WYLOSOWANO: [ {rzut_koscia(kod_kosci)} ]")

            elif opcja == '2':
                try:
                    prog = int(input("Podaj próg punktów (np. 50): "))
                    wynik_gry = tryb_gry(kod_kosci, prog)
                    print(f"\n--- WYNIK GRY ---")
                    print(f"Rundy: {wynik_gry['liczba_rund']} | Suma: {wynik_gry['koncowa_suma']}")
                    print(f"Rzuty: {wynik_gry['historia_rzutow']}")
                except ValueError:
                    print("BŁĄD: Wpisz liczbę całkowitą!")

            elif opcja == '3':
                try:
                    ile = int(input("Ile rzutów? "))
                    if ile <= 0:
                        print("BŁĄD: Podaj liczbę większą od zera!")
                        continue
                    wyniki = symulacja_masowa(kod_kosci, ile)
                    stats = oblicz_statystyki(wyniki)
                    print(f"\n--- STATYSTYKI ({ile} rzutów) ---")
                    for k, v in stats.items():
                        print(f"{k.capitalize()}: {v:.2f}" if isinstance(v, float) else f"{k.capitalize()}: {v}")
                except ValueError:
                    print("BŁĄD: Wpisz prawidłową liczbę!")
        else:
            print("Niepoprawny wybór.")

if __name__ == "__main__":
    interaktywne_menu()
