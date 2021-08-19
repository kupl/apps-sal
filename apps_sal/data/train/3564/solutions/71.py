def stringy(size):
    count = 3
    arr = ''
    for i in range(size):
        if count % 2 == 1:
            arr += '1'
            count += 1
        else:
            arr += '0'
            count += 1
    return arr
