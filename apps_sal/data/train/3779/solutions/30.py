def convert_SI(val, unit_in, unit_out='ms'):
    SI = {'ms': 0.001, 's': 1, 'm': 60, 'h': 60 * 60}
    return val * SI[unit_in] / SI[unit_out]


def past(*args, order='hms'):
    return sum((convert_SI(x, u) for (u, x) in zip(order, args)))
