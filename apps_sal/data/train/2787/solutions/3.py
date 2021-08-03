def inverse_slice(items, a, b):
    return [v for i, v in enumerate(items) if i < a or i >= b]
