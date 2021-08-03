def vowel_2_index(string):
    return ''.join([str(c + 1) if l.lower() in 'aeiou' else l for c, l in enumerate(string)])
