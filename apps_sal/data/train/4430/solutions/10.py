def vowel_2_index(string):
    return ''.join((str(i) if c in 'aeiouAEIOU' else c for (i, c) in enumerate(string, 1)))
