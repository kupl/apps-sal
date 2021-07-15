from re import findall

def solve(s):
    return max(map(len, findall("[aeiou]+", s)))
