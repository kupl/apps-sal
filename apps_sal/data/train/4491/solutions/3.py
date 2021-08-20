def solve(a, b):
    res = ''
    for char in a + b:
        if char in a and char in b:
            continue
        res += char
    return res
