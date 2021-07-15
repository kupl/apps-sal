def sequence_sum(start, stop, step):
    strides = (stop - start) // step
    return 0 if start > stop else (strides + 1) * (step * strides/2 + start)
