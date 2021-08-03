from operator import add, mul
from itertools import count


def array_conversion(arr):
    for i in count():
        if len(arr) == 1:
            return arr[0]
        arr = list(map((add, mul)[i & 1], arr[::2], arr[1::2]))
