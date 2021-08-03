def sort_emotions(arr, order):
    return sorted(arr, key=[':D', ':)', ':|', ':(', 'T_T'].index, reverse=not order)
