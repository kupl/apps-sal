def digits(n):
    return map(int, str(n))


def repeat_sequence_len(n):
    seen = []
    while n not in seen:
        seen.append(n)
        n = sum((x * x for x in digits(n)))
    return len(seen) - seen.index(n)
