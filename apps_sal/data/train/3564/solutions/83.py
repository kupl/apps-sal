from itertools import islice, cycle
def stringy(size):
    return ''.join(str(i) for i in islice(cycle([1, 0]), 0, size))
