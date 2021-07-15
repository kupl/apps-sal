def divide(weight: int) -> bool:
    """ Check whether Pete and Billy can divide the melons so that each of them gets an even amount. """
    return not weight % 2 if weight != 2 else False
