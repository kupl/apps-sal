def loneliest(number):
    xs = [int(c) for c in str(number)]
    d = {i: sum(xs[max(i - x, 0):i] + xs[i + 1:i + 1 + x]) for i, x in enumerate(xs)}
    m = min(d.values())
    return any(xs[i] == 1 and d[i] == m for i in d)
