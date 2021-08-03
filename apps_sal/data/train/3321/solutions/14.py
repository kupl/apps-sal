def evil(n):
    n = (n & 0x5555555555555555) + ((n >> 1) & 0x5555555555555555)
    n = (n & 0x3333333333333333) + ((n >> 2) & 0x3333333333333333)
    n = (n & 0x0F0F0F0F0F0F0F0F) + ((n >> 4) & 0x0F0F0F0F0F0F0F0F)
    n = (n & 0x00FF00FF00FF00FF) + ((n >> 8) & 0x00FF00FF00FF00FF)
    n = (n & 0x0000FFFF0000FFFF) + ((n >> 16) & 0x0000FFFF0000FFFF)
    n = (n & 0x00000000FFFFFFFF) + ((n >> 32) & 0x00000000FFFFFFFF)

    return "It's Odious!" if n % 2 == 1 else "It's Evil!"
