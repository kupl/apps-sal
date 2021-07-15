def solve(s):
    if s.islower() or s.isupper():
        return s
    else:
        if len([i for i in s if i.isupper()]) > len([i for i in s if i.islower()]):
            return s.upper()
        else:
            return s.lower()
