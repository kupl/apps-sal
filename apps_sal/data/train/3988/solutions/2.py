import re

def encode(s):
    return "".join(f"{len(g)}{c}" for g, c in re.findall(r"((.)\2*)", s))
    
def decode(s):
    return "".join(int(n) * c for n, c in re.findall(r"(\d+)(\w)", s))
