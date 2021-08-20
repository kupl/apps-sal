def replace_exclamation(s):
    test = 'aeiouAEIOU'
    return ''.join(('!' if i in test else i for i in s))
