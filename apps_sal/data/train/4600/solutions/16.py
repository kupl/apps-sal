def move_zeros(array):
    strs = []
    array1 = array.copy()
    for i in array1:
        if isinstance(i, str):
            strs.append(i)
            array1[array1.index(i)] = ' '
    for i in array1:
        array1[array1.index(i)] = str(array1[array1.index(i)])
    for i in array1:
        if i == '0' or i == '0.0':
            array1.remove(i)
            array1.append('0')
    for i in array1:
        if i != ' ':
            array1[array1.index(i)] = eval(array1[array1.index(i)])

    def insf():
        v = 0
        while v < len(strs):
            v += 1
            yield v
    n = insf()
    for i in array1:
        if i == ' ':
            array1[array1.index(i)] = strs[next(n) - 1]
    return array1
