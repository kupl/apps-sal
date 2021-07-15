def length_of_sequence(arr,n):
    pos = [i for i, x in enumerate(arr) if x == n]
    return pos[1] - pos[0] + 1 if len(pos) == 2 else 0
