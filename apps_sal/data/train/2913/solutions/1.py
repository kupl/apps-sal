(f, e) = '■□'


def x(n):
    l = n // 2
    middle = [f'{e * l}{f}{e * l}']
    half = [f'{e * i}{f}{e * (n - 2 * i - 2)}{f}{e * i}' for i in range(l)]
    return '\n'.join(half + middle + half[::-1])
