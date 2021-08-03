def next_item(xs, item):
    flag = False
    for el in xs:
        if flag:
            return el
        if el == item:
            flag = True
