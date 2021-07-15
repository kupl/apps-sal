import re

def calculate(s):
    xs = re.split(r'(plus|minus)', s)
    xs[::2] = map(int, xs[::2])
    return str(xs[0] + sum(
        xs[i+1] * (1 if xs[i] == 'plus' else -1)
        for i in range(1, len(xs), 2)
    ))
