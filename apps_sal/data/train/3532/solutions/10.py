def apple(x):
    msg0 = "It's hotter than the sun!!"
    msg1 = 'Help yourself to a honeycomb Yorkie for the glovebox.'
    return [msg1, msg0][int(x) ** 2 >= 1000]
