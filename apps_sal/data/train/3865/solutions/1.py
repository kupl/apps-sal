def looper(start, stop, number):
    if number == 1:
        return [start]
    elif number == 2:
        return [start, stop]
    increment = (stop - start) / (number - 1)
    arr = []
    for n in range(0, number - 1):
        new_element = start + n * increment
        arr.append(new_element)
    arr.append(float(stop))
    return arr
