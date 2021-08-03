def super_size(n):
    list1 = []
    for i in str(n):
        list1.append(i)
    list1.sort()
    list1.reverse()
    return int(''.join(list1))
