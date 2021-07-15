def pre_fizz(n):
    arr = []
    counter = 1
    for i in range(n):
        arr.append(counter)
        counter += 1
    return arr
