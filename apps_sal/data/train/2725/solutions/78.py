def gimme(input_array):
    a = input_array.index(max(input_array))
    b = input_array.index(min(input_array))
    
    for i in [0,1,2]:
        if i not in [a,b]:
            return i
            break

