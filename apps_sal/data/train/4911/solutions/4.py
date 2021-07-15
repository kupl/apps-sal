def sum_arrays(arrays, shift):
    dummy_arr = [ 0 for i in range(len(arrays[0])+(len(arrays)-1)*shift)]
    modified_arrays = []
    for i in range(len(arrays)):
        modified_arrays.append([0 for temp in range(i*shift)])
        modified_arrays[i] += arrays[i]
        if len(modified_arrays[i]) < len(dummy_arr):
            modified_arrays[i] += [0 for temp in range(len(dummy_arr) -len(modified_arrays[i]) )]
    for i in range(len(dummy_arr)):
        for arr in modified_arrays:
            dummy_arr[i] += arr[i]
        
    
    return dummy_arr
