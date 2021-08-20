def next_item(xs, item):
    print(isinstance(xs, range))
    i = 0
    for num in xs:
        if i == 1:
            return num
        if num == item:
            i += 1
    return None
