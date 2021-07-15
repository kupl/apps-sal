def max_tri_sum(numbers):
    numberlist = []
    accumulator = 0
    for eachnumber in numbers:
        if eachnumber in numberlist:
            continue
        else:
            numberlist.append(eachnumber)
    numberlist.sort()
    for eachnumber in numberlist[-3:]:
        accumulator = accumulator + eachnumber
    return accumulator
