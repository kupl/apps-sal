from itertools import zip_longest, chain
vowels = {'a', 'e', 'i', 'o', 'u'}

def solve(s):
    vow, con = [], []
    for c in s: (con, vow)[c in vowels].append(c)
    if abs(len(con) - len(vow)) > 1: return "failed"
    vow.sort(); con.sort()
    x, y = (vow, con) if len(vow) >= len(con) else (con, vow)
    return ''.join(chain.from_iterable(zip_longest(x, y, fillvalue='')))
