def to_freud(sentence):
    if sentence == '':
        return ''
    lista = sentence.split(' ')
    output = 'sex ' * len(lista)
    return output[:-1]
