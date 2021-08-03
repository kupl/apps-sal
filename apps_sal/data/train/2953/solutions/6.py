def numericals(s):
    d = {x: 0 for x in s}
    result = []
    for symbol in s:
        d[symbol] += 1
        result.append(str(d[symbol]))
    return ''.join(result)
