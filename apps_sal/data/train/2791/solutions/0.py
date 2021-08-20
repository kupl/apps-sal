def trigrams(phrase):
    phrase = phrase.replace(' ', '_')
    return ' '.join([phrase[i:i + 3] for i in range(len(phrase) - 2)])
