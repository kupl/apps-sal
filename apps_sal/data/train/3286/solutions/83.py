def enough(cap, on, wait):
    """ return wait list if bus is full"""
    wait_list = on + wait - cap
    return (wait_list > 0) * wait_list
