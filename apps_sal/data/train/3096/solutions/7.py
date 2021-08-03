def josephus(items, k):
    cursor = 0
    killed = []
    while len(items):
        cursor = (cursor + k - 1) % len(items)
        killed.append(items.pop(cursor))

    return killed
