from itertools import cycle
seq = {'fib': [0, 0, 0, 1], 'pad': [0, 1, 0, 0], 'jac': [0, 0, 0, 1], 'pel': [0, 0, 0, 1], 'tri': [0, 0, 0, 1], 'tet': [0, 0, 0, 1]}
pat = {'fib': 'a[-1]+a[-2]', 'pad': 'a[-2]+a[-3]', 'jac': 'a[-1]+2*a[-2]', 'pel': '2*a[-1]+a[-2]',
       'tri': 'a[-1]+a[-2]+a[-3]', 'tet': 'a[-1]+a[-2]+a[-3]+a[-4]'}


def zozonacci(pattern, length):
    if not pattern:
        return []
    a = seq[pattern[0]][:length]
    c = cycle(pattern)
    for i in range(length - 4):
        a.append(eval(pat[next(c)]))
    return a
