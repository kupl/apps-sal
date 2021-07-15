move_zeros = lambda arr: [i for i in arr if str(i) == 'False' or i != 0] + [_ for _ in arr if str(_) != 'False' and _ == 0]
