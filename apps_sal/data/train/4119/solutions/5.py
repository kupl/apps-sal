val = {':D': 4, ':)': 3, ':|': 2, ':(': 1, 'T_T': 0}.__getitem__


def sort_emotions(arr, order):
    return sorted(arr, reverse=order, key=val)
