def tr(n):
    return sum((int(i) ** 2 for i in str(n)))


def repeat_sequence_len(n):
    if n < 10:
        return n
    tmp = []
    n = tr(n)
    while n not in tmp:
        tmp.append(n)
        n = tr(n)
    return len(tmp) - tmp.index(n)
