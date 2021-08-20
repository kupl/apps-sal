def sort_twisted37(arr):

    def key(x):
        return int(str(x).translate(str.maketrans('37', '73')))
    return sorted(arr, key=key)
