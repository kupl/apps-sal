def animals(heads, legs):
    b = legs / 2 - heads
    a = heads - b
    if int(a) < 0 or int(b) < 0:
        return 'No solutions'
    elif int(a) != float(a) or int(b) != float(b):
        return 'No solutions'
    elif int(a) == 0 and int(b) == 0:
        return (0, 0)
    else:
        return (int(a), int(b))
