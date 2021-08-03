def sort_by_bit(lst):
    return sorted(lst, key=lambda n: (f"{n:b}".count("1"), n))
