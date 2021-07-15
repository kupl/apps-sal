def to_freud(sentence):
    result = ''
    new_sentence = sentence.split(' ')
    for word in range(len(new_sentence)):
        new_sentence[word] = 'sex'
        result += new_sentence[word] + ' '
    return result[:-1]
