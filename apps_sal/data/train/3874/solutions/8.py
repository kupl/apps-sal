def sort_twisted37(arr):
    return sorted(arr, key=lambda x: int(str(x).translate(str.maketrans('37', '73'))))
