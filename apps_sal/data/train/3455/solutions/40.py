def disarium_number(number):
    nms = [int(x) for x in str(number)]
    o = 0
    for (n, i) in enumerate(nms):
        o += i ** (n + 1)
    if o == number:
        return 'Disarium !!'
    else:
        return 'Not !!'
