from itertools import count


def array_conversion(arr):
    for i in count(1):
        it = iter(arr)
        arr = [a + b if i % 2 else a * b for a, b in zip(it, it)]
        if len(arr) == 1:
            return arr.pop()
