tr = str.maketrans('37', '73')


def sort_twisted37(arr):
    return sorted(arr, key=lambda n: int(str(n).translate(tr)))
