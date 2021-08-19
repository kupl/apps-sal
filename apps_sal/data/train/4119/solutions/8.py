def sort_emotions(arr, order):
    order_dict = {':D': 1, ':)': 2, ':|': 3, ':(': 4, 'T_T': 5}
    return sorted(arr, key=lambda x: order_dict[x], reverse=not order)
