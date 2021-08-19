from operator import sub


def find_pattern(sequence):
    result = list(map(sub, sequence[1:], sequence))
    size = len(result)
    for i in range(1, size + 1):
        (q, r) = divmod(size, i)
        if r == 0:
            check = result[:i]
            if check * q == result:
                return check
