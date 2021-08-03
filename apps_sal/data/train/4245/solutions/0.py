def explode(arr):
    return [arr] * sum(v for v in arr if isinstance(v, int)) or 'Void!'
