def solve(lst):
    a, b, c = lst[0] < lst[1], lst[1] < lst[2], lst[-1] < lst[0]
    m = a if a == b else c
    return ('R' if c == m else '') + ('A' if m else 'D')
