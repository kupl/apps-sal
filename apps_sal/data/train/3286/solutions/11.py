def enough(cap, on, wait):
    """
    :param cap: total number of seats
    :param on: number of passengers on the bus
    :param wait: number of passengers waiting for the bus
    :return: number of passengers that can't enter the bus
    """
    if wait - (cap - on) < 0:
        return 0
    else:
        return wait - (cap - on)
