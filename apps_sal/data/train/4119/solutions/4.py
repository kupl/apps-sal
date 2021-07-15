def sort_emotions(arr, order):
    return sorted(arr, key=lambda x: ['T_T', ':(', ':|', ':)', ':D'].index(x), reverse=order)
