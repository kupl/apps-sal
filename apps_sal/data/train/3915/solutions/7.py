def carry(s):
    a,b = s.split()
    c,f = 0,0
    for i,j in zip(map(int,a[::-1]),map(int,b[::-1])):
        if i+j+f > 9:
            f = 1
            c += 1
        else:
            f = 0
    return c

def solve(s):
    r = list(map(carry,s.splitlines()))
    return '\n'.join('No carry operation' if x==0 else f'{x} carry operations' for x in r)
