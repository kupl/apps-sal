def domain_name(url):
    napis = url

    if "//" in napis:
        tab = napis.split("//")
        czlon = tab[1]
        print(czlon[0])
    else:
        czlon = napis

    if not czlon.startswith("www"):
        zmienna = czlon.split(".")
        print(zmienna[0])
        wynik = zmienna[0]
    else:
        zmienna = czlon.split(".")
        print(zmienna[1])
        wynik = zmienna[1]
    return wynik
