import re

CONS_PAT = re.compile(r"[^aeiuo]+")

def solve(s):
    return max(sum(map(lambda c: ord(c)-96, conss)) for conss in CONS_PAT.findall(s))
