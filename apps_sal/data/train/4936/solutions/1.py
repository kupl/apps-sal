def reverse(lst):
    out = list()
    for i in range(len(lst)-1,-1,-1):
        out.append(lst[i])
    return out
