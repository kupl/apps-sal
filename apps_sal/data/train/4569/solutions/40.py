def next_item(my_list, item):
    found = None
    for x in my_list:
        if found:
            return x
        if x == item:
            found = True
    return None
