mystery = lambda n: n ^ (n >> 1)
def mystery_inv(n):
    m = n >> 1
    while m != 0:
        n ^= m
        m >>= 1
    return n
name_of_mystery = lambda: 'Gray code'
