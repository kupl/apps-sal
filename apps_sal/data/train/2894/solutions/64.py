def triple_trouble(one, two, three):

    my_list = []
    for i in range(len(one)):
        my_list.append((one[i] + two[i] + three[i]))

    final = ''.join(my_list)
    
    return final
