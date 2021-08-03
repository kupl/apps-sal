def promenade(choices):
    if not choices:
        return (1, 1)
    (a, b) = promenade(choices[1:])
    return (a, a + b) if choices[0] == 'L' else (a + b, b)
