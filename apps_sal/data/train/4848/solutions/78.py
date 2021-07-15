def char_freq(message):
    diccionario = {}
    for x in message: 
        if x in diccionario: 
            diccionario[x] += 1
        else: 
            diccionario[x] = 1    
    return diccionario
