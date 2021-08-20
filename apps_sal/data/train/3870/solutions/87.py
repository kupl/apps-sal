def solve(s):
    wordSizes = [len(x) for x in s.split()]
    reversedS = s.replace(' ', '')[::-1]
    o = []
    for x in wordSizes:
        o.append(reversedS[:x])
        reversedS = reversedS[x:]
    return ' '.join(o) if s[-1] is not ' ' else ' '.join(o) + ' '
