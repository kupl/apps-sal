def merge_arrays(first, second):
    first.sort()
    second.sort()
    third = first + second
    ls = []
    for i in third:
        if i in ls:
            continue
        ls.append(i)
    ls.sort()
    return ls
