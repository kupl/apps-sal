def enough(cap, on, wait):
    if cap - on - wait < 0:
        seats_left = cap - on
        return wait - seats_left
    else:
        return 0
