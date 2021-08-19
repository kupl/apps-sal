from collections import deque


def count_targets(n, sequence):
    q = deque(sequence[:n], maxlen=n)
    return sum(((x == q[0], q.append(x))[0] for x in sequence[n:]))
