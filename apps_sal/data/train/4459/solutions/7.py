def nth_even(n):
    maListe = range(n * 2)
    for elem in maListe[::-1]:
        if elem % 2 == 0:
            return elem
