def gimme(input_array):
    sort_items = []
    for i in input_array:
        sort_items.append(i)
    sort_items.sort()
    y = 0
    for i in input_array:
        if i == sort_items[1]:
            av = y
            break
        y += 1
    return y
