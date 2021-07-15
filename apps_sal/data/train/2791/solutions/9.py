def trigrams(phrase):
    if len(phrase) < 3:
        return ''
    phrase = phrase.replace(' ', '_')
    ret = []
    for i in range(len(phrase) - 2):
        ret.append(phrase[i:i + 3])
    return ' '.join(ret)
