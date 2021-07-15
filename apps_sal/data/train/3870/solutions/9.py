def solve(s):
    tempr = list(s)
    ts = tempr.count(' ')
    for i in range(ts):
        tempr.remove(' ')
    tempr = tempr[::-1]
    s = list(s)
    it = 0
    iw = 0
    while iw != len(s):
        if s[iw] == ' ':
            iw+=1
        else:
            s[iw] = tempr[it]
            it+=1
            iw+=1
    return ''.join(s)
