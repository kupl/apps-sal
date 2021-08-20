def reverse(lst):
    ret = []
    while lst:
        ret.append(lst[-1])
        lst = [a - b for (a, b) in zip(lst, lst[1:])]
    return ret[::-1]
