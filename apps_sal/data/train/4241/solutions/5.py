
def sequence_sum(start, stop, step):
    return sum(range(start, stop + 1, step))


def range_sum(n):
    return n * (n + 1) / 2


def multiples_sum(divisor, n):
    return range_sum(n // divisor) * divisor


def sequence_sum(start, stop, step):
    diff = stop - start
    return 0 if start > stop else start * (diff // step + 1) + multiples_sum(step, diff)


def sequence_sum(start, stop, step):
    strides = (stop - start) // step
    return 0 if start > stop else (strides + 1) * (step * strides / 2 + start)
