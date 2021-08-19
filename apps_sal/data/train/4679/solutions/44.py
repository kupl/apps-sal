def to_freud(sentence):
    result = ''
    for i in sentence.split(' '):
        result += 'sex '
    return result.rstrip(' ')
    # return ["sex" for i in sentence.split(' ')]
