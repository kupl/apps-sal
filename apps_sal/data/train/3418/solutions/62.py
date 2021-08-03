def reverse_list(l):
    i = 0
    size = len(l)
    while i < size:
        temp = l.pop(size - 1 - i)
        l.append(temp)
        i += 1
    return l
