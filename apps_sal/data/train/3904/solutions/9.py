from itertools import product

def is_divisible_by_6(string):
    result = []
    n = 0
    indices = []
    for i, c in enumerate(string):
        if c == '*':
            n += 1
            indices.append(i)

    s = list(string)
    for combo in product(list(map(str, range(10))), repeat=n):
        for idx, digit in zip(indices, combo):
            s[idx] = digit
        if int(''.join(s)) % 6 == 0:
            result.append(''.join(s))
        
    return result
