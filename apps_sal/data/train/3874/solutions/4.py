def sort_twisted37(lst):
    return sorted(lst, key=comp)


def comp(n):
    return int(str(n).translate(str.maketrans("37", "73")))
