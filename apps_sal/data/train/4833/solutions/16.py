def replace_exclamation(s):
    return ''.join(['!' if i in 'aeiouAEIOU' else i for i in s])
