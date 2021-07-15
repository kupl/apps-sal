def next_item(xs, item):
    done = False
    for i in xs:
        if done == True:
            return i
        if i == item:
            done = True
    return None

