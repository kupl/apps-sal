def switcheroo(string):
    swap = {'a': 'b', 'b': 'a'}
    return ''.join((swap.get(ch, ch) for ch in string))
