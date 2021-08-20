def fixed_xor(a, b):
    m = min(len(a), len(b))
    return f'{int(a[:m], 16) ^ int(b[:m], 16):0{m}x}' if m else ''
