def apple(x):
    return {
        True: "It's hotter than the sun!!",
        False: "Help yourself to a honeycomb Yorkie for the glovebox."
    }[int(x) * int(x) > 1000]
