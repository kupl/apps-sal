def make_desc_order(arr):
    return arr[::-1] if arr and arr[0] < arr[-1] else arr

def merge_arrays_gen(*args):
    arr1, arr2 = (make_desc_order(arr) for arr in args)    
    while arr1 or arr2:
        if arr1 and arr2:
            yield arr1.pop() if arr1[-1] < arr2[-1] else arr2.pop()
        elif arr1:            
            yield arr1.pop()
        else:
            yield arr2.pop()

merge_arrays = lambda *args: list(dict.fromkeys(merge_arrays_gen(*args)))
