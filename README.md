# Radar Vols Montréal

Page publique : https://nguefackuriel.github.io/radar-vols-montreal/

Billets d'avion aller-retour nettement sous leur prix habituel, au départ de Montréal (YUL) et des aéroports voisins (YQB, YOW, BTV, PBG).

- `index.html` : la page. Elle lit `deals.json` à chaque ouverture.
- `deals.json` : les aubaines en cours, réécrit par l'agent à chaque balayage (deux fois par jour).
- `tools/build_deals.py` : assemble `deals.json` à partir d'un export de la base de l'agent.

Chaque prix est relevé sur Google Flights puis vérifié aux dates exactes. Une aubaine n'est publiée que si Google Flights classe le prix « bas » et que le rabais atteint au moins 15 % du prix habituel. Les tarifs changent vite : vérifiez le prix final avant de payer.
