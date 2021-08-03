def array_madness(a, b):
    array1 = 0
    array2 = 0
    for v in a:
        array1 += v**2
    for v in b:
        array2 += v**3
    return array1 > array2
