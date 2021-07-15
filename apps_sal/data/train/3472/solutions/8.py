def next_day_of_week(d, a):
    t = a & ~((1 << d) - 1) or a
    return (t & -t).bit_length()
