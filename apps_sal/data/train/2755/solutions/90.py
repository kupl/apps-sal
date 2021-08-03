def multiple_of_index(arr):
    new_array = []
    counter = 0
    for i in arr:
        if counter != 0:
            if i % counter == 0:
                new_array.append(i)
        counter += 1
    return(new_array)
