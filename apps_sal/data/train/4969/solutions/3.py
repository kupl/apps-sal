def tower_builder(n, block):
    w, h = block
    return [f"{'*' * w * (2*i + 1):^{(n*2 - 1) * w}}" for i in range(n) for _ in range(h)]
