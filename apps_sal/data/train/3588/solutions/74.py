def quadratic(x1, x2):
    int(x1)
    int(x2)
    thisdict = {'a': 1, 'b': -x1 + -x2, 'c': -x1 * -x2}
    return (thisdict.get('a'), thisdict.get('b'), thisdict.get('c'))
