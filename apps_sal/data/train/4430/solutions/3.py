def vowel_2_index(string):
    return ''.join([str(i + 1) if x.lower() in 'aeiou' else x for (i, x) in enumerate(string)])
