def between(a, b):
    assert a < b
    array = []

    for i in range(a, b + 1):
        array.append(i)
    return array
