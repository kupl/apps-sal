def repeater(string, n):
    strout = [[char for char in string] for x in range(n)]
    fix = [y for x in strout for y in x]
    out = ''.join(map(str,fix))
    return out
