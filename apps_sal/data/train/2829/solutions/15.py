def array_madness(a, b):
    list1 = []
    list2 = []
    for i in a:
        list1.append(i ** 2)
    for j in b:
        list2.append(j ** 3)
    if sum(list1) > sum(list2):
        return True
    elif sum(list1) < sum(list2):
        return False
    elif sum(list1) == sum(list2):
        return True
    else:
        return True
