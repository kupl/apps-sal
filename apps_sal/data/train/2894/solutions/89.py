def triple_trouble(one, two, three):
    
    char = ""
    for i, j, k in zip(one, two, three):
        char += (str(i) + str(j) + str(k))
    return char
