def replace_exclamation(s):
    return eval('s' + ''.join((".replace('%s','!')" % i for i in 'aeiouAEIOU')))
