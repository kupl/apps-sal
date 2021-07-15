def solve(s):
    return [sum(i==ord(a.lower())-ord('a') for i, a in enumerate(s[j])) for j, _ in enumerate(s)]
