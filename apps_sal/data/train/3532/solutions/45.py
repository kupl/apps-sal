def apple(x):
    x = int(x) if isinstance(x, str) else x
    if x ** 2 > 1000:
        return "It's hotter than the sun!!"
    else:
        return "Help yourself to a honeycomb Yorkie for the glovebox."
