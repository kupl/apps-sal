def vowel_2_index(string):
    vowels = frozenset('aeiouAEIOU')
    return ''.join([str(i + 1) if c in vowels else c for (i, c) in enumerate(string)])
