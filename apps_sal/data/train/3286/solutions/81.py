def enough(cap, on, wait):
    seat = cap - on - wait
    return 0 if seat >= 0 else abs(seat)
