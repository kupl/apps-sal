def find_average(array):
    tot = 0
    if array:
        for n in array:
            tot += n
        return tot / len(array)
    else:
        return 0
