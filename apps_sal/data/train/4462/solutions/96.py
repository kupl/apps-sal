def adjacent_element_product(array):
    print(array)
    i = 1
    rtot = array[0]*array[1]
    while i+1 <= len(array):
        if array[i]*array[i-1] >= rtot:
            rtot = array[i]*array[i-1]
            print(rtot)
        i += 1
    return rtot
