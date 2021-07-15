trans = str.maketrans("37", "73")
twist = lambda n: int(str(n).translate(trans))

def sort_twisted37(arr):
    return sorted(arr, key=twist)
