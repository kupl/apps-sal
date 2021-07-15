def reverse_list(l):
    a = []
    for i in range(0, len(l)):
        a.append(l[-1 - i])
    return a
