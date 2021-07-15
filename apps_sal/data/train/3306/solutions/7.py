import re

def solve(a,b):
    pattern = f'^{a.replace("*", ".*")}$'
    return bool(re.match(pattern, b))

