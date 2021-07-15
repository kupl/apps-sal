def gimme(input_array):
    i=0
    while i<3:
        c=input_array[i]
        if c<max(input_array) and c>min(input_array):
            return input_array.index(c)
            break
        else:
            i+=1
