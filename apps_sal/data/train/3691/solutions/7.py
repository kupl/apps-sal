def get_a_down_arrow_of(n, s=0):
    return '' if n < 1 else ' ' * s + '1' if n == 1 else '\n'.join([' ' * s + ''.join([str(q % 10) for q in range(1, n + 1)] + [str(q % 10) for q in range(n - 1, 0, -1)])] + [get_a_down_arrow_of(n - 1, s + 1)])
