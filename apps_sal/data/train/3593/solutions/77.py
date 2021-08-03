def capitalize(s, ind):
    tulos = ""

    for i in range(0, len(s)):
        merkki = s[i]
        if (i in ind):
            merkki = merkki.upper()
        tulos += merkki

    return tulos
