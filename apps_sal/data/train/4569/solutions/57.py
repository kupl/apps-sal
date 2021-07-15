def next_item(xs, item):
    flag = False
    
    for x in xs:
        if flag == True:
            return x
        if item == x:
            flag = True

