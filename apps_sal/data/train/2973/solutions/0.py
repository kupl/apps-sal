def array_conversion(arr):
    sign = 0
    while len(arr) > 1:
        sign = 1^sign
        arr = list(map(lambda x, y: x+y, arr[0::2],arr[1::2]) if sign else map(lambda x, y: x*y, arr[0::2],arr[1::2]))
    return arr[0]
