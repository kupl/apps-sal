def capitalize(s):
    string_even, string_odd = [], []
    for i, n in enumerate(s):
        if i % 2 == 0:
            string_even.append(n.upper())
        else:
            string_even.append(n)

    for i, n in enumerate(s):
        if i % 2 != 0:
            string_odd.append(n.upper())
        else:
            string_odd.append(n)
    return [''.join(string_even), ''.join(string_odd)]


"""
def capitalize(s):
    string_even = ''.join([c.upper() if not (i % 2) else c for i, c in enumerate(x)])
    string_odd = ''.join([c.upper() if i % 2 else c for i, c in enumerate(x)])
    return [string_even, string_odd]
"""
