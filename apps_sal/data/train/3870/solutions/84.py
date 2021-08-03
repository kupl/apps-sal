def solve(s):
    l = [c for c in s.replace(" ", "")]
    return ''.join([" " if c == " " else l.pop() for c in s])
