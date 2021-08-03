def sort_array(source_array):
    odd = sorted(list(filter(lambda x: x % 2, source_array)))
    l, c = [], 0
    for i in source_array:
        if i in odd:
            l.append(odd[c])
            c += 1
        else:
            l.append(i)
    return l
