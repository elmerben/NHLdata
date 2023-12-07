import json

def haePelaaja(kohteet):
    haettava = input("nimi: ").lower()
    for kohde in kohteet:
        if kohde["name"].lower() == haettava:
            return kohde


def listaaJoukkueet(kohteet, valinta):
    if valinta == 2:
        juttu = "team"
    elif valinta == 3:
        juttu = "nationality"
    lista = []
    for kohde in kohteet:
        if kohde[juttu] not in lista:
            lista.append(kohde[juttu])
    lista.sort()    
    for asia in lista:
        print(asia)


def joukkueenPelaajat(kohteet, valinta):
    if valinta == 4:
        juttu = "team"
        joukkue = input("joukkue: ")

    elif valinta == 5:
        juttu = "nationality"
        joukkue = input("maan pelaajat: ")

    lista = []
    for kohde in kohteet:
        if kohde[juttu] == joukkue:
            lista.append(kohde)
    listajarjestys = sorted(lista, key=lambda x: x['goals'] + x['assists'], reverse= True)
    for ukko in listajarjestys:
        tulostus(ukko)


def enitenPisteita(kohteet):
    maara = int(input("kuinka monta pelaajaa haluat listata? "))
    jarjestetty = sorted(kohteet, key=lambda x :(x['goals'] + x['assists'], x['goals']), reverse= True)
    for ukko in jarjestetty[:maara]:
        tulostus(ukko)


def enitenMaaleja(kohteet):
    maara = int(input("kuinka monta pelaajaa haluat listata? "))
    jarjestetty = sorted(kohteet, key=lambda x :(x['goals'], -x['games']), reverse= True)
    for ukko in jarjestetty[:maara]:
        tulostus(ukko)


def tulostus(asia):
    print(f"{asia['name']:<21}{asia['team']:<5}{asia['goals']:>2} + {asia['assists']:>2} = {asia['goals'] + asia['assists']:>3}")



def main():
    kohde = "kaikki.json"
    with open(kohde) as tiedosto:
        data = tiedosto.read()
    kohteet = json.loads(data)
    print(f"luettiin {len(kohteet)} pelaajan tiedot")
    print("")
    print("komennot: \n0 lopeta \n1 hae pelaaja \n2 joukkueet\n3 maat\n4 joukkueen pelaajat\n5 maan pelaajat\n6 eniten pisteitä\n7 eniten maaleja")

    while True:
        try:
            valinta = int(input("komento: "))
            if valinta == 0:
                break
            elif valinta == 1:
                asia = haePelaaja(kohteet)
                tulostus(asia)
            elif valinta == 2: 
                listaaJoukkueet(kohteet, valinta)
            elif valinta == 3:
                listaaJoukkueet(kohteet, valinta)
            elif valinta == 4:
                joukkueenPelaajat(kohteet, valinta)
            elif valinta == 5:
                joukkueenPelaajat(kohteet, valinta)
            elif valinta == 6:
                enitenPisteita(kohteet)
            elif valinta == 7:
                enitenMaaleja(kohteet)
        except ValueError:
            print("Virheellinen syöte.")


main()