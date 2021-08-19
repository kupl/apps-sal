def feast(beast, dish):
    beast.replace(' ', '')
    beast_ls = [x for x in beast]
    dish.replace(' ', '')
    dish_ls = [x for x in dish]
    if beast_ls[0] == dish_ls[0] and beast_ls[-1] == dish_ls[-1]:
        return True
    else:
        return False
