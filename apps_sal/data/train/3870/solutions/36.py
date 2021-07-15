def solve(s):
    u = []
    reversed_list = list(s[::-1].replace(' ', ''))
    [u.append(reversed_list.pop(0) if c.isalpha() else ' ') for c in s]
    return "".join(u)
