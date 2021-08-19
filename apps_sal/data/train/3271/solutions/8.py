def arr(n=''):
    n = str(n)
    if len(n) == 0:
        return []
    n = int(n)
    array = []
    for i in range(n):
        array.append(i)
    return array
