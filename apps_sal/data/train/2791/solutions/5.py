def trigrams(phrase):
    p = phrase.replace(' ','_')
    return ' '.join([p[i:i+3] for i in range(len(p)-2)])

