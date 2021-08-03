def create_array(num):
    array = []
    i = 1
    while num >= i:
        array.append(i)
        i += 1
    return array


print(create_array(5))
