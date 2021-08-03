def get_min_max(seq):
    min = seq[0]
    max = seq[0]
    for number in seq:
        if number > max:
            max = number

    for number in seq:
        if number < min:
            min = number

    return (min, max)
