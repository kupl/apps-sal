def inverse_slice(items, a, b):
    return list(i for i in items if i not in items[a:b])
