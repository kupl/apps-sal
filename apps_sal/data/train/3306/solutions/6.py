import re

def solve(a,b):
    pattern = a.replace("*", ".*")
    return bool(re.fullmatch(pattern, b))
