def apple(x):
    x = int(x)

    def g(x):
        return x * x
    if g(x) > 1000:
        return "It's hotter than the sun!!"
    else:
        return 'Help yourself to a honeycomb Yorkie for the glovebox.'
