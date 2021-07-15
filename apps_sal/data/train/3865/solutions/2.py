def iter(start, number, step):
    for i in range(number-1):
        yield float(start + step*i)

def looper(start, stop, number):
    if number == 1:
        return [start]

    step = (stop - start) / (number - 1)
    lt = list(iter(start, number, step))
    lt.append(stop)
    return lt
