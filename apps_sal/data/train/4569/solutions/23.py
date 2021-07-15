def next_item(xs, item):
    flag = False
    for element in xs:
        if flag:
            return element
        if element == item:
            flag = True
    return None
        

