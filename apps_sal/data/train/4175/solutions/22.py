def repeater(string, n):
    collection = []
    while n > 0:
        collection.append(string)
        n -= 1
    return ''.join(collection)
