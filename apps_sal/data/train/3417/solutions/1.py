def cut_the_ropes(arr):
    qty = len(arr)
    sorted_ropes = sorted(arr)
    return [qty - sorted_ropes.index(n) for n in sorted(set(arr))]

