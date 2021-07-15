def feast(beast, dish):
    b_list = list(beast)
    d_list = list(dish)
    if b_list[0] == d_list[0] and b_list[-1] == d_list[-1]:
        return True
    else:
        return False
