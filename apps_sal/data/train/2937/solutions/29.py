def between(a, b):
    difference = 0
    diff_range = b - a + 1
    new_list = []
    for x in range(diff_range):
        new_list.append(a + difference)
        difference += 1
    return new_list
