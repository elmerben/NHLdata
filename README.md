# NHL Pelaajatietokanta

Tämä projekti on Python-skripti, joka mahdollistaa jääkiekkoilijoiden tilastotietojen selaamisen
ja analysoinnin käyttämällä avoimen datan `kaikki.json`-tiedostoa, joka sisältää NHL-pelaajien tilastotietoja.

## Ominaisuudet

- **Hae Pelaaja**: Hae tiettyä pelaajaa nimen perusteella.
- **Listaa Joukkueet**: Näytä kaikki joukkueet tai maat, joista pelaajia on tilastossa.
- **Joukkueen Pelaajat**: Listaa kaikki tietyssä joukkueessa tai tietyistä maista olevat pelaajat.
- **Eniten Pisteitä**: Näytä pelaajat, joilla on eniten pisteitä (maalit + syötöt).
- **Eniten Maaleja**: Näytä pelaajat, joilla on eniten maaleja.

## Tiedoston Rakenne

- `nhl_data.py`: Pääskriptitiedosto.
- `kaikki.json`: JSON-tiedosto, joka sisältää pelaajatiedot.
