def array_madness(a, b):
    if sum(list(map(lambda x: x * x, a))) > sum(list(map(lambda x: x * x * x, b))):
        return True
    else:
        return False
