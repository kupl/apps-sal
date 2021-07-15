import math
def find_longest(arr):
    x = arr[0]
    for each in arr:
        if len(str(each)) > len(str(x)):
            x = each
    return x
