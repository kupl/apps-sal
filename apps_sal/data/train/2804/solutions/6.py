def custom_christmas_tree(chars, n):
    chars *= n*n
    s = lambda n: (n+1)*n//2
    pad = lambda s: ' '*(n-len(s)//2-1)+s
    row = lambda i: pad(' '.join(chars[s(i):s(i)+i+1]))
    return '\n'.join([*map(row,range(n))] + [pad('|')]*(n//3))
