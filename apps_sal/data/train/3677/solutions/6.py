def f(array):
    if array == [] : return False
    return all([type(array[0]) == type(e) for e in array])

def filter_homogenous(arrays):
    return [a for a in arrays if f(a)]

