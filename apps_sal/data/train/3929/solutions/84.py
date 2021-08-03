def reverse(st):
    salida = []
    word = ""
    for i in range(len(st)):
        if st[i] == " " or i == len(st):
            if word != "":
                salida.append(word)

            salida.append(st[i])
            word = ""
        else:
            word += st[i]

    salida.append(word)
    a = "".join(salida[::-1]).replace("  ", " ")
    return a.replace("  ", " ").strip(" ")
