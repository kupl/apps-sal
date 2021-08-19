def shared_bits(a, b):
    return sum((ai == bi == '1' for (ai, bi) in zip(f'{a:b}'[::-1], f'{b:b}'[::-1]))) >= 2
