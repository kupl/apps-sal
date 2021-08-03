def array_madness(a, b):
    squared = list(map(lambda x: x * x, a))
    cubed = list(map(lambda x: x * x * x, b))
    if sum(squared) > sum(cubed):
        return True
    return False
