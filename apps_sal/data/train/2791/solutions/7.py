def trigrams(phrase):
    if len(phrase) < 3:
        return ''
    phrase = phrase.replace(' ', '_')
    chars = [x for x in phrase]
    trigram = []
    for x in range(1, len(chars) - 1):
        trigram.append(chars[x - 1] + chars[x] + chars[x + 1])
    return ' '.join(trigram)
