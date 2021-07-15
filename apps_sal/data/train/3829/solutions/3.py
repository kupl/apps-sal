def build_square(blocks):
    x1, x2, x3, x4 = (blocks.count(n) for n in range(1, 5))
    b3 = min(x3, x1)
    b2 = min(x2 % 2, (x1 - b3) // 2)
    b1 = (x1 - b3 - b2 * 2) // 4
    return x4 + b3 + x2 // 2 + b2 + b1 > 3 

