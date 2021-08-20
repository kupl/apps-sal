rank = {x: i for (i, x) in enumerate([':D', ':)', ':|', ':(', 'T_T'])}


def sort_emotions(arr, order):
    return sorted(arr, key=rank.get, reverse=not order)
