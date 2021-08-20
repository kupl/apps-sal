def explode(arr):
    return [arr] * sum((x for x in arr if type(x) == int)) or 'Void!'
