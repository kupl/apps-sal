def well(x):
    good_count = 0
    for i in x:
        if i == "good":
            good_count += 1

    if 0 < good_count <= 2:
        return 'Publish!'
    if good_count == 0:
        return 'Fail!'
    if good_count > 2:
        return 'I smell a series!'
