def enough(cap, on, wait):
    cant = cap - on - wait
    if cant >= 0:
        return 0
    else:
        return abs(cant)
