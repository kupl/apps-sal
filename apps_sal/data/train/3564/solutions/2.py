from itertools import cycle, islice

def stringy(size):
    return ''.join(islice(cycle('10'), size))
