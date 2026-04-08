# 🎲 Symulator Rzutu Kością - Projekt Zaliczeniowy

[![CI](https://github.com/jakubpijanka05/Symulator-rzutu-koscia/actions/workflows/ci.yml/badge.svg)](https://github.com/jakubpijanka05/Symulator-rzutu-koscia/actions)

Projekt stworzony w ramach zajęć, wykorzystujący zautomatyzowany Pipeline CI/CD oraz konteneryzację Docker.

---

## 👥 Skład Grupy
* **Lider:** Jakub Pijanka (102150)
* **Członek 2:** Paweł Adamkiewicz (104307)
* **Członek 3:** Hubert Kurkowiak (101608)
* **Członek 4:** Patryk Kucharski (101569)

---

## 📝 Opis projektu
Aplikacja napisana w języku Python symulująca rzuty różnymi typami kości (np. **k4, k6, k20**). Program posiada zaimplementowany tryb gry, tryb masowej symulacji oraz moduł zbierania i obliczania statystyk rzutów (suma, średnia, wartości skrajne).

---

## 🚀 Instrukcja uruchomienia (Docker Hub)

Aplikacja została opublikowana jako gotowy obraz. Nie musisz instalować środowiska Python – wystarczy Docker.

**W terminalu z zainstalowanym Dockerem, wykonaj poniższą komendę:**

```bash
docker run -it kuba15251/symulator-kosci:latest
