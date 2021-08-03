def stringy(size):
    i = 0
    list1 = ['1']
    for n in range(size - 1):
        if i % 2 == 0:
            list1.append('0')
            i += 1
        else:
            list1.append('1')
            i += 1
    return ''.join(list1)
