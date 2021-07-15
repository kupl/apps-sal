def diff(arr):
    #your code here
    vals = [abs(eval(pair)) for pair in arr]
    return False if all(val == 0 for val in vals) else arr[vals.index(max(vals))]
    return val
