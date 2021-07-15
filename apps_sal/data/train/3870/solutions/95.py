def solve(s):
    spaces = []
    soln = ''
    for i in range(len(s)):
        if s[i] == ' ':
            spaces.append(i)
    for x in s[::-1]:
        if x == ' ':
            continue
        else:
            soln += x
    for x in spaces:
        soln = soln[:x] + ' ' + soln[x:]
    return soln
