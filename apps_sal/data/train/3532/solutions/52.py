def apple(x):
    x = int(x)
    s = x**2
    if s>1000:
        return "It's hotter than the sun!!"
    else:
        return 'Help yourself to a honeycomb Yorkie for the glovebox.'
e = apple("60")
print(e)
