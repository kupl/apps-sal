def gimme(input_array):
    max_i = input_array.index(max(input_array))
    min_i = input_array.index(min(input_array))
    
    middle_i = [i for i in range(len(input_array)) if i not in [max_i,min_i]][0]
    
    return middle_i
