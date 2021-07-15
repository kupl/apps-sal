import re
def solve(s):
    result = list(s)
    indices = [m.span()[0] for m in re.finditer(r"[^ ]", s)]    
    for a,b in zip(indices, indices[::-1]):
        result[a] = s[b]
    return "".join(result)
