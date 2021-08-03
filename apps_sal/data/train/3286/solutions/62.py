def enough(cap, on, wait):
    if cap - on >= wait:  # capacity minus bus occupancy more or equal than of people waiting
        return 0  # If there is enough space, return 0.
    else:
        return abs(cap - (on + wait))  # and if there isn't, return the number of passengers he can't take
        # abs() function: return absolute values of a num.
