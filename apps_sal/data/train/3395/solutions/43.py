def remove_duplicate_words(s):
    cadena = s.split()
    cadena2 = []
    cadena3 = " "
    for i in cadena:
        if i in cadena2:
            pass
        else:
            cadena2.append(i)
    cadena3 = cadena3.join(cadena2)
    return cadena3
