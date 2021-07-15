def to_freud(sentence):
    result = ''
    for i in range(len(sentence.split(' '))):
        result+='sex '
    return result[:-1]
