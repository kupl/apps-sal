def solution(pairs):
    l = []
    for a in pairs:
        l.append((str(a) + " = " + str(pairs[a])))
    return ','.join(sorted(l))
