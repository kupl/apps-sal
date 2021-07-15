def move_zeros(array):
    new_list = []
    c = 0
    for item in array:
        if item != 0 or type(item) == bool:
            new_list.append(item)
        else:
            c += 1
    i = 0
    while i < c:
        new_list.append(0)
        i+=1
    return new_list

