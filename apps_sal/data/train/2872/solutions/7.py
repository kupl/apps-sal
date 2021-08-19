def coin(n):
    f = f'{{:0{n}b}}'
    t = str.maketrans('01', 'HT')
    return [f.format(k).translate(t) for k in range(2 ** n)]
