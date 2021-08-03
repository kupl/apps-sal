def reverse_list(l):
    rev = []
    up = len(l) - 1

    for i in range(up, -1, -1):
        rev.append(l[i])

    return rev
