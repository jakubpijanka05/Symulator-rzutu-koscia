def interaktywne_menu():
    print("\n" + "="*40)
    print(" PROFESJONALNY SYMULATOR KOŚCI RPG ")
    print("="*40)
    
    while True:
        print("\nWYBIERZ TRYB:")
        print("[1] Pojedynczy rzut")
        print("[2] Tryb Gry (rzuty aż do progu punktów)")
        print("[3] Symulacja masowa + Statystyki")
        print("[0] Wyjście z programu")
        
        opcja = input("\nTwój wybór: ").strip()

        if opcja == '0':
            print("Zamykanie symulatora. Powodzenia!")
            break

        if opcja in ['1', '2', '3']:
            kosc = input("Wybierz kość (4, 6 lub 20): ").strip()
            if kosc not in ['4', '6', '20']:
                print("BŁĄD: Obsługujemy tylko kości 4, 6 i 20. Spróbuj ponownie.")
                continue
            
            kod_kosci = f"K{kosc}"

            if opcja == '1':
                wynik = rzut_koscia(kod_kosci)
                print(f"\n>>> WYLOSOWANO: [ {wynik} ]")

            elif opcja == '2':
                try:
                    prog = int(input("Podaj próg punktów do wygranej (np. 50): "))
                    wynik_gry = tryb_gry(kod_kosci, prog)
                    print(f"\n--- WYNIK GRY DO {prog} PKT ---")
                    print(f"Liczba rund: {wynik_gry['liczba_rund']}")
                    print(f"Końcowa suma: {wynik_gry['koncowa_suma']}")
                    print(f"Historia rzutów: {wynik_gry['historia_rzutow']}")
                except ValueError:
                    print("BŁĄD: Próg musi być liczbą całkowitą!")

            elif opcja == '3':
                try:
                    ile = int(input("Ile rzutów wykonać w symulacji? "))
                    if ile <= 0:
                        print("BŁĄD: Liczba rzutów musi być większa od zera!")
                        continue
                        
                    wyniki_sym = symulacja_masowa(kod_kosci, ile)
                    stats = oblicz_statystyki(wyniki_sym)
                    
                    print(f"\n--- STATYSTYKI SYMULACJI ({ile} rzutów) ---")
                    for klucz, wartosc in stats.items():
                        print(f"{klucz}: {wartosc}")
                        
                except ValueError:
                    print("BŁĄD: Liczba rzutów musi być wpisana cyframi!")

        else:
            print("Niepoprawny wybór. Wpisz 1, 2, 3 lub 0.")

if __name__ == "__main__":
    interaktywne_menu()
