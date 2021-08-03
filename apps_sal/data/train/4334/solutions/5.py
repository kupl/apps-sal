def gen_fib():
    a, b = 1, 1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b


def skiponacci(n):
    result = []
    for i, f in enumerate(gen_fib()):
        if i == n:
            break
        result.append(str(f) if i % 2 == 0 else 'skip')
    return ' '.join(result)
