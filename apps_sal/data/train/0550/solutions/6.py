from math import log2


def rotate(n, bits):
    if(n & 1):
        n = n >> 1 | 1 << bits
    else:
        n = n >> 1
    return n


t = int(input())
while(t > 0):
    t -= 1
    max_xor = 0
    count = 0
    max_count = 0
    a, b = map(int, input().split())
    a_bits = int(log2(a) + 1)
    b_bits = int(log2(b) + 1)
    if(a_bits > b_bits):
        bits = a_bits
    else:
        bits = b_bits
    c = bits
    bits -= 1
    while(c > 0):
        c -= 1
        c_xor = a ^ b
        if(c_xor > max_xor):
            max_xor = c_xor
            max_count = count
        b = rotate(b, bits)
        count += 1
    print(max_count, max_xor)
