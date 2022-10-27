# Oblig3-FredrikAndersen

Jeg har fulgt eksempler fra forelesningen 19. oktober CI/CD for å sette opp github actions, og endret litt av koden i main.yml for å kjøre testene ved hjelp av pytest.
Github actions er satt opp til å kjøre ved push til main, og vil da sette opp python 3.10, installere pytest 7.1.3 (hentet fra requirements.txt) og kjøre pytest på en ubuntu-server med nye versjon.

Etter å ha satt opp github actions har jeg sjekket at testene kjører ved å endre på en test slik at den feiler og dermed se at den også feiler i github etter å ha pushet koden. Jeg har også sett at exit-codes til pytest stemmer overens med det som forventes når testene passerer, ikke kjøres og noen av testene ikke passerer.
