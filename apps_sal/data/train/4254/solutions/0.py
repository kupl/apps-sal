import re

def solve(eq):
    return ''.join(reversed(re.split(r'(\W+)', eq)))
