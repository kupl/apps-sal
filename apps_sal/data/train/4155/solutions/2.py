def solve(a, b):
    tr = str.maketrans('0123456789', '01----9-86')
    return sum((1 for x in map(str, range(a, b)) if x == ''.join(reversed(x.translate(tr)))))
