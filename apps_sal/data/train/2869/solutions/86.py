def distinct(seq):
    salida = []

    for elmnt in seq:
        if elmnt not in salida:
            salida.append(elmnt)

    return salida
