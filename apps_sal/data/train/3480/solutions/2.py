def sequence_sum(start, stop, step):
    n = (stop - start) // step
    last = start + n * step
    return (n + 1) * (start + last) // 2 if n >= 0 else 0
