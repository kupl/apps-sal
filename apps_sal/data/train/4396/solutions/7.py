def freq_seq(s, sep):
    numero = len(s)
    conta = 0
    contatore = 0
    contatore1 = 0
    lista = []
    while conta != numero:
        z = str(s[conta])
        while contatore1 < numero:
            if z == s[contatore1]:
                contatore += 1
            contatore1 += 1
        contatore1 = 0
        lista.append(str(contatore))
        contatore = 0
        conta += 1
    x = sep.join(lista)
    return x
