def smash(words):
    if words==[]:
        return ''
    else:
        frase = words[0]
        for word in words[1:]:
            frase = frase+' ' +word
        return frase
