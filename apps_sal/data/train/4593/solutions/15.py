def make_desc_order(arr):
    return arr[::-1] if arr and arr[0] < arr[-1] else arr


def merge_arrays_gen(*args):
    (arr1, arr2) = (make_desc_order(arr) for arr in args)
    while arr1 or arr2:
        yield (arr1.pop() if not arr2 or (arr1 and arr1[-1] < arr2[-1]) else arr2.pop())


merge_arrays = lambda *args: list(dict.fromkeys(merge_arrays_gen(*args)))
