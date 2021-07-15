def get_temp(x):
    return "It's hotter than the sun!!" if x**2 > 1000 else 'Help yourself to a honeycomb Yorkie for the glovebox.' 

def apple(x):
    if isinstance(x, int):
        return get_temp(x)
    else:
        return get_temp(int(x))
