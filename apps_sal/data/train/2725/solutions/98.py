def gimme(input_array):
    a = list()
    print(a, input_array)
    x = 0
    for i in input_array:
        print("i:", i)
        a.append(i)

    input_array.sort()
    for i in a:

        if i == input_array[1]:
            break
        x += 1
    print(a, input_array)

    return x
