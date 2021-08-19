from collections import deque
start = {'fib': [0, 0, 0, 1], 'jac': [0, 0, 0, 1], 'pad': [0, 1, 0, 0], 'pel': [0, 0, 0, 1], 'tet': [0, 0, 0, 1], 'tri': [0, 0, 0, 1]}
sum_idx = {'fib': [-1, -2], 'jac': [-1, -2, -2], 'pad': [-2, -3], 'pel': [-1, -1, -2], 'tet': [-1, -2, -3, -4], 'tri': [-1, -2, -3]}


def sequence(pattern):
    (pattern, seq) = (deque(pattern), deque(start[pattern[0]]))
    while 1:
        seq.append(sum((seq[idx] for idx in sum_idx[pattern[0]])))
        yield seq.popleft()
        pattern.rotate(-1)


def zozonacci(pattern, length):
    return pattern and [n for (_, n) in zip(range(length), sequence(pattern))]
