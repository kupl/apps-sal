def gimme(input_array):
    l2=input_array.copy()
    l2.sort()
    mid_element=l2[1]
    index_mid_element=input_array.index(mid_element)
    return (index_mid_element)

