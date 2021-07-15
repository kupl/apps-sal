from itertools import chain

gen = lambda x: chain(range(1, x+1), range(x, 0, -1))
concat = lambda x: ' '.join(str(y%10) for y in gen(x))
padding = lambda size: lambda x: f"{concat(x): >{size}}"

def stairs(n):
    return '\n'.join(map(padding(4*n-1), range(1, n+1)))
