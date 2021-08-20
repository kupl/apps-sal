def apple(x):
    if type(x) == str:
        temp = int(x)
    else:
        temp = x
    if temp ** 2 > 1000:
        return "It's hotter than the sun!!"
    else:
        return 'Help yourself to a honeycomb Yorkie for the glovebox.'
