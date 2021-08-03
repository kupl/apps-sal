def vowel_2_index(string):
    vowels = 'aeiouAEIOU'
    return ''.join(str(i) if v in vowels else v for i, v in enumerate(string, 1))
