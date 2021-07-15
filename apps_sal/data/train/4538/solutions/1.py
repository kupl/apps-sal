def reverse_fun(n):
    l = len(n)
    return ''.join(b+a for a,b in zip(list(n[:l//2])+[''], n[l//2:][::-1]))
