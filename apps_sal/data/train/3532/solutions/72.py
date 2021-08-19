def apple(x):
    if type(x) is str:
        x = int(x)
    return "It's hotter than the sun!!" if x * x > 1000 else 'Help yourself to a honeycomb Yorkie for the glovebox.'
