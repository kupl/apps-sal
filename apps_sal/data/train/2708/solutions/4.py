def yes_no(arr):
    new = []
    take = True
    while arr:
        if take:
            some = arr.pop(0)
            new.append(some)
            take = False
        else:
            some = arr.pop(0)
            arr.append(some)
            take = True
    return new
