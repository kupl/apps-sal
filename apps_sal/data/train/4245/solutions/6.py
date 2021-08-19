def explode(arr):
    return [arr] * sum((x for x in arr if isinstance(x, int))) or 'Void!'
