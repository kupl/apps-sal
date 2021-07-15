def solve(s):
    return max([ int(i) for i in ''.join([i if i.isdigit()else' 'for i in s]).split() ])
