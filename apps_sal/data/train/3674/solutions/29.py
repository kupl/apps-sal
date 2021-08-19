def add_binary(a, b):
    # your code here
    res = a + b  # sum first
    buf = ''
    while res >= 1:  # since the number in binary can be represented as
        # a reverse of remainders of series of it divisions
        # by 2 - we'll do the divisions first...
        buf += str(res % 2)
        res = res // 2
    buf = buf[::-1]  # ...and then reverse the string
    return buf
