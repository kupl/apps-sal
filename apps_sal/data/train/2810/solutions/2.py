from operator import eq
from string import ascii_lowercase

def solve(strings):
    return [sum(map(eq, s.lower(), ascii_lowercase)) for s in strings]
