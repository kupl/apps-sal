def solve(s):
    return 1 == ((sum([op!=code for (op, code) in zip(s[0:len(s)//2:1], s[-1:len(s)//2-1:-1])]))|(len(s)%2))
