def two_highest(arg1):
    if type(arg1) is str:
        return False
    else:
        l = [i for i in set(arg1)]
        result = []
        j = 0
        for i in l:
            result.append(max(l))
            l.remove(max(l))
            j += 1
            if j == 2:
                break
    return result
