def trigrams(phrase):
    phrase = phrase.replace(' ', '_')
    return ' '.join((''.join(xs) for xs in zip(phrase, phrase[1:], phrase[2:])))
