from numpy import base_repr


def gen(s):
    for i, c in zip(reversed(range(len(s))), s):
        if c == '2':
            raise Exception
        if c == '1':
            yield f"3^{i}"


def sum_of_threes(n):
    try:
        return '+'.join(gen(base_repr(n, 3)))
    except:
        return "Impossible"
