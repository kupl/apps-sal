def no_space(x):
    resultado = ''
    for i in range(len(x)):
        if x[i] != ' ':
            resultado += x[i]
    return resultado
