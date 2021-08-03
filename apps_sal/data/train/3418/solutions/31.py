def reverse_list(l):
    x = []
    for i in range(1, len(l) + 1):
        x.append(l[-i])
    return x
