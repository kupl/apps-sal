def apple(x: int) -> str:
    """ Get a message based on squared `x` parameter. """
    return ('Help yourself to a honeycomb Yorkie for the glovebox.', "It's hotter than the sun!!")[pow(int(x), 2) > 1000]
