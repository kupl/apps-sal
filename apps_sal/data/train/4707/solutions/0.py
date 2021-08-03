def to_bytes(n):
    if not n:
        return ['00000000']

    res = []
    while n:
        res.append('{:08b}'.format(n % 256))
        n //= 256

    return res[::-1]
