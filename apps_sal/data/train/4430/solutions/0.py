def vowel_2_index(string):
    vowels = 'aeiouAEIOU'
    return ''.join(x if x not in vowels else str(n + 1) for n,x in enumerate(string))
