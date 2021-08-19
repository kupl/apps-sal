def lowercase_count(strng):
    l_1 = list(strng)
    l_2 = list('qwertyuiopasdfghjklzxcvbnm')
    l_3 = []
    for elem in l_1:
        if elem in l_2:
            l_3.append(elem)
    return len(l_3)
