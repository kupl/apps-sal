def reverse_list(l):
    re = []
    for i in range(0, len(l)):
        re.append(l.pop())
    return re
