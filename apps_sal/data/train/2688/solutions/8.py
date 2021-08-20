def f(n):
    return sum((int(d) ** 2 for d in str(n)))


def repeat_sequence_len(n):
    S = []
    while n not in S:
        S.append(n)
        n = f(n)
    return len(S) - S.index(n)
