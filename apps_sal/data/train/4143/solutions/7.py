def points(string):
    lista = list(string)
    lista_1 = sorted(lista)
    if len(set(string)) == 1:
        return 50
    if len(set(string)) == 2:
        if lista_1[0] == lista_1[1] and lista_1[3] == lista_1[4]:
            return 30
        else:
            return 40
    if len(set(string)) == 5:  # Aici trebuie lucrat
        valoare = 0
        if int(lista_1[3]) - int(lista_1[2]) == 1 and int(lista_1[4]) - int(lista_1[3]) == 1:
            valoare = 1
        if valoare == 1:
            return 20
        if valoare == 0:
            return 0
    else:
        return 0
