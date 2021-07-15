def inverse_slice(items, a, b):
    c = items[a:b]
    for i in c:
        items.remove(i)
    return items
