def strongest_even(n, m):
    while n <= m:
        prev = n
        n += 1 << strongness(n)
    return prev

def strongness(n):
    return n.bit_length() - len(format(n, 'b').rstrip('0'))
