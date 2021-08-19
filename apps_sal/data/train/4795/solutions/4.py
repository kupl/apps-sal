V = 'aeouiAEOUI'


def flesch_kincaid(text):
    sentences = text.count('.') + text.count('!') + text.count('?')
    words = text.count(' ') + 1
    syllables = sum((p not in V and c in V for (p, c) in zip(' ' + text, text)))
    return round(0.39 * words / sentences + 11.8 * syllables / words - 15.59, 2)
