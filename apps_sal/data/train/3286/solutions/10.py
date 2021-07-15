def enough(cap, on, wait):
# See if there is enough room
    if cap - on >= wait:
        return 0                  # This means enough room for those waiting
    else:
        return wait - cap + on    # This is the number of those who cannot get on
