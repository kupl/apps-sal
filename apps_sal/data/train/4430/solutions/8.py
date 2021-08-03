def vowel_2_index(string):
    return ''.join(c if c not in 'aeiouAEIOU' else str(i + 1) for i, c in enumerate(string))
