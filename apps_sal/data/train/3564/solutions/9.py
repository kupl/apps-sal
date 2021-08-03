def stringy(size):
    arr = []
    for i in range(size):
        if i % 2 == 0:
            arr.append('1')
        else:
            arr.append('0')
    return ''.join(arr)
