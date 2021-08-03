def getCarrycount(a, b):
    r, index = 0, 0
    al = [int(d) + int(f) for d, f in zip(reversed(list(a)), reversed(list(b)))]
    for item in al:
        index = (item + index) // 10
        r += index
    return r


def solve(input_string):
    lnumber = [tuple(item.split()) for item in input_string.split('\n')]
    lsum = [getCarrycount(z[0], z[1]) for z in lnumber]
    return '\n'.join('{} carry operations'.format(n) if n else 'No carry operation' for n in lsum)
