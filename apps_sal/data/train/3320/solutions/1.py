ORDER = 'one two three four five six'.split()[::-1]
TBL = {'ttt': '----x----', 'htt': '---------', 'hht': '---- ----', 'hhh': '----o----'}


def oracle(arr):
    d = {n: TBL[''.join(sorted(rest))] for (n, *rest) in arr}
    return '\n'.join((d[o] for o in ORDER))
