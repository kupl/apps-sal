import re


def solve(s):
    ops, parts = [], ['']
    for c in re.findall(r'\d*\(|\)|[a-z]+', s):
        if c == ')':
            segment = parts.pop()
            parts[-1] += ops.pop() * segment
        elif not c[0].isalpha():
            ops.append(int(c[:-1]) if c[0] != '(' else 1)
            parts.append('')
        else:
            parts[-1] += c
    return parts[0]
