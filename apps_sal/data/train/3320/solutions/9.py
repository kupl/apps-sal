d = {'one': 5, 'two': 4, 'three': 3, 'four': 2, 'five': 1, 'six': 0}
ok = {(2, 1): '---- ----', (1, 2): '---------', (3, 0): '----o----', (0, 3): '----x----'}


def oracle(a):
    return '\n'.join([ok[i[1:].count('h'), i[1:].count('t')] for i in sorted(a, key=lambda x: d[x[0]])])
