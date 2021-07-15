def solve(s):
    a = [i for i in s if i.lower() != i]
    return s.upper() if len(a) > len(s)/2 else s.lower()
