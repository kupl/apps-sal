def solve(s):
    i=j=0
    i=len([i+1 for a in [*s] if a.isupper()])
    j=len([j+1 for a in [*s] if a.islower()])
    return s.lower() if i<j or i==j else s.upper()

