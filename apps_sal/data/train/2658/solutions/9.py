def countSetBits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count


def convert_bits(a, b):
    return countSetBits(a ^ b)
