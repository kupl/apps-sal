def every(arr, interval=1, start=0):
    flt = arr[start:]
    return list(flt[::interval])
