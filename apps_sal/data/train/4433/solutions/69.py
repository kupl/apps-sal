def logical_calc(arr, log):
    x = {'AND': 'and', 'OR': 'or', 'XOR': '!='}
    y = arr.pop(0)
    while len(arr) > 0:
        y = eval(str(y) + f' {x[log]} ' + str(arr.pop(0)))
    return y
