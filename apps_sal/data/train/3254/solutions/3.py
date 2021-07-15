def any_odd(x):
    return int("1" in f"{x:032b}"[::2])
