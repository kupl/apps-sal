def solve(s):
    l = 0
    h = 0
    for i in s:
        if ord(i) < 91:
            h += 1
        else:
            l +=1
    return s.upper() if h>l else s.lower()
