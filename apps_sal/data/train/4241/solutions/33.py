def sequence_sum(begin_number, end_number, step):
    x = begin_number
    st = begin_number + step

    if begin_number > end_number:
        return 0
    else:
        while st <= end_number:
            x += st
            st += step

        return x
