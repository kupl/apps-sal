def apple(x):
    x = int(x) if isinstance(x, str) else x
    return 'It\'s hotter than the sun!!' if x * x > 1000 else 'Help yourself to a honeycomb Yorkie for the glovebox.'
