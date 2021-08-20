def solve(s):
    return s.lower() if sum((1 for i in s if i in 'abcdefghijklmnopqrstuvwxyz')) >= len(s) / 2 else s.upper()
