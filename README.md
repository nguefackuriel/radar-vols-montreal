# Radar Vols Montréal

Page publique : https://nguefackuriel.github.io/radar-vols-montreal/

Billets d'avion aller-retour nettement sous leur prix habituel, au départ de Montréal (YUL) et des aéroports voisins (YQB, YOW, BTV, PBG), et hôtels en rabais dans 25 villes du Canada.

- `index.html` : la page (onglets Vols et Hôtels). Elle lit `data.json` à chaque ouverture.
- `data.json` : les aubaines en cours (vols et hôtels), réécrit par l'agent à chaque balayage (deux fois par jour).
- `tools/build_data.py` : assemble `data.json` à partir d'un export de la base de l'agent.

Chaque prix est relevé sur Google Flights puis vérifié aux dates exactes. Une aubaine n'est publiée que si Google Flights classe le prix « bas » et que le rabais atteint au moins 15 % du prix habituel. Les tarifs changent vite : vérifiez le prix final avant de payer.

Hôtels : chaque rabais repéré sur Google Hôtels est vérifié sur la fiche de l'hôtel aux dates exactes. Un hôtel n'est publié que si Google dit que ses prix sont « actuellement bas », avec au moins 20 % de rabais, une note d'au moins 3,5 sur 5 et au moins 100 avis.
