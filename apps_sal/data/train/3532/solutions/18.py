def apple(x):

    if type(x) is int:
        n = x
        if n ** 2 > 1000:
            return "It's hotter than the sun!!"
        else:
            return "Help yourself to a honeycomb Yorkie for the glovebox."

    elif type(x) is str:
        n = int(x)
        if n ** 2 > 1000:
            return "It's hotter than the sun!!"
        else:
            return "Help yourself to a honeycomb Yorkie for the glovebox."
