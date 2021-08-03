def multiple_of_index(arr):
    vList = []
    for key, value in enumerate(arr):
        if key == 0:
            continue
        if value % key == 0:
            vList.append(value)

    return vList
