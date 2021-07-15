def arr(n=0):
    print(type(n))
    array = []
    for x in range(n):
        array.append(x)
        print (type(array[x]))
    return array
