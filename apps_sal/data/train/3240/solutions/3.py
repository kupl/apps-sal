def true_binary(n):
    return [1 if d == '1' else -1 for d in (f'1{n >> 1:b}' if n > 1 else '1')]
