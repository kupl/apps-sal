from math import floor

def func(arr):
    x = floor(sum(arr)/len(arr))
    return [x] + [format(x, f'{i}') for i in 'box']
