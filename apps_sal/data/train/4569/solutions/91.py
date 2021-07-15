def next_item(xs, item, flag=0):
    for i in xs:
        if flag == 1: return i
        if i == item: flag = 1
