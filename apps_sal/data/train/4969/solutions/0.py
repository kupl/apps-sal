def tower_builder(n, (w, h)):
    return [str.center("*" * (i*2-1)*w, (n*2-1)*w) for i in range(1, n+1) for _ in range(h)]
