trans = str.maketrans('37', '73')


def twist(n):
    return int(str(n).translate(trans))


def sort_twisted37(arr):
    return sorted(arr, key=twist)
