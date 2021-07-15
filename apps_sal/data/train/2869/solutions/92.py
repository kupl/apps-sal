def distinct(seq):
    item = []
    for i in seq:
        if i not in item:
            item.append(i)
    return item            
