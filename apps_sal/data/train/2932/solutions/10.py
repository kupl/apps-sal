def colour_association(arr):
    dict1 = []
    for item in arr:
        dicts = {}
        dicts.update({item[0]: item[1]})
        dict1.append(dicts)

    print(dict1)
    return dict1
