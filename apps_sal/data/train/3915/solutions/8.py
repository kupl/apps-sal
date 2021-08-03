def carry(x, y):
    x = [*map(int, x[::-1])]
    y = [*map(int, y[::-1])]
    r = 0
    c = 0
    for a, b in zip(x, y):
        v = a + b + c
        if v > 9:
            r += 1
        c = v // 10
    return f'{r} carry operations' if r else 'No carry operation'


def solve(input_string):
    return'\n'.join(carry(*s.split())for s in input_string.split('\n'))
