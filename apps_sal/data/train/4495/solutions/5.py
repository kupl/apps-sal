def am_I_afraid(day, num):
    # your code here
    rep = False
    lst1 = [('monday', 12), ('wednesday', 34), ('thursday', 0), ('saturday', 56), ('sunday', 666), ('sunday', -666)]

    input = (day.lower(), num)

    if input in lst1 or (input[0] == 'tuesday' and input[1] > 95) or (input[0] == 'friday' and input[1] % 2 == 0):
        rep = True
    return rep
