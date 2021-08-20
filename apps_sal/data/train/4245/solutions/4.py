def explode(a):
    return [a] * sum((e for e in a if type(e) == int)) or 'Void!'
