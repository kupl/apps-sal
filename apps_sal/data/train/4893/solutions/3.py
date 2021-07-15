from itertools import chain

def wave_sort(a):
    for i, x in zip(chain(range(1, len(a), 2), range(0, len(a), 2)), sorted(a)):
        a[i] = x
