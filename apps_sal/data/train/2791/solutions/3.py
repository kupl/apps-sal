def trigrams(phrase):

    s = phrase.replace(' ', '_')

    return ' '.join(s[i:i + 3] for i in range(len(s) - 2))
