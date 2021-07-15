def array_manip(array):
    result = []
    for i in range(len(array)):
        try:
            cr = array[i]
            mm = sorted(x for x in array[i+1:] if x > cr)[0]
            result.append(mm)
        except:
            result.append(-1)
    return result
