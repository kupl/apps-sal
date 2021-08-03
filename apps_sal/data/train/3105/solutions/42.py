def count_sheep(n):
    frase = " sheep..."
    pecore = ""
    for i in range(n):
        pecore += str(i + 1) + frase
    return pecore
