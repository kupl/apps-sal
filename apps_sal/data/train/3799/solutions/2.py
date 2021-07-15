def baubles_on_tree(baubles, branches):
    if branches == 0:
        x = "Grandma, we will have to buy a Christmas tree first!"
        return x
    x = baubles // branches
    list_of_baubles = [x]*branches
    z = (baubles % branches)
    y = z - 1
    if z != 0:
        for i in range(z):
            list_of_baubles[i] = list_of_baubles[i]+1
    
    return list_of_baubles
