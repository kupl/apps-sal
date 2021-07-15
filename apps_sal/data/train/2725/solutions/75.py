def gimme(input_array):
    # Implement this function
    array=sorted(input_array);
    mid_num=array[int((len(array)-1)/2)]
    return(input_array.index(mid_num))


