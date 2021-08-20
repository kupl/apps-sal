from bisect import bisect_left
ns = [n * (n + 1) // 2 for n in range(1000)]


def get_participants(handshakes):
    return bisect_left(ns, handshakes) + 1
