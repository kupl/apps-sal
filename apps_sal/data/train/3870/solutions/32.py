def solve(s):
    rev_s  = [c for c in s if c != ' ']
    return ''.join([rev_s.pop() if c != ' ' else ' ' for c in s])
    

