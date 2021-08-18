def gimme(input_array):
    sort = sorted(input_array)
    x = sort[1]
    leng = len(input_array)

    if sum(input_array) < 0:
        sort = reversed(sort)

    for i in range(leng):
        if x == input_array[i]:
            return i
