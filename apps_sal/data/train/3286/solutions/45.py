def enough(cap, on, wait):
    people_left = wait - (cap - on)
    if people_left <= 0:
        return 0
    if people_left > 0:
        return people_left
