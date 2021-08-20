import re


def solve(s):
    (c, v) = (sorted(re.findall('[^aeiou]', s)), sorted(re.findall('[aeiou]', s)))
    (m, n) = (max(c, v, key=len), min(c, v, key=len)) if len(v) != len(c) else (v, c)
    return ''.join(sum(zip(m, n + ['']), ())) if abs(len(v) - len(c)) <= 1 else 'failed'
