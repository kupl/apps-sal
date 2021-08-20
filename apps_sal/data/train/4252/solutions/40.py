def merge_arrays(first, second):
    s = first + second
    s.sort()
    l = []
    for i in s:
        if i not in l:
            l.append(i)
    return l
