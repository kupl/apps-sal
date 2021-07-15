def replace_exclamation(s):
    e = lambda _: '!' if _ in 'aeiouAEIOU' else _
    return ''.join([e(x) for x in s])
