def merge_arrays(first, second):
    cool = list(set(first + second))
    cool.sort()
    return cool
