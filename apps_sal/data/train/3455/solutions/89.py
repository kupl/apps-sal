def disarium_number(number):
    result = [int(i) for i in str(number)]
    arr = []
    for (j, i) in enumerate(result, start=1):
        m = [j, i]
        x = i ** j
        arr.append(x)
        s = sum(arr)
    if s == number:
        return 'Disarium !!'
    else:
        return 'Not !!'
