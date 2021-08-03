def sort_array(source_array):
    odd = []
    for i in source_array:
        if i % 2 == 1:
            odd.append(i)
    odd.sort()
    x = 0
    for j in range(len(source_array)):
        if source_array[j] % 2 == 1:
            source_array[j] = odd[x]
            x += 1

    return source_array
