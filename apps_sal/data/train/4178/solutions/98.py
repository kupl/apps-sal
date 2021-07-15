def min_sum(arr: list) -> int:
    sorted_arr = sorted(arr)
    arr_len_half = len(arr)//2
    start_arr_half = sorted_arr[:arr_len_half]
    end_arr_half = sorted_arr[arr_len_half:]
    result_sum = 0
    
    for start_num, end_num in zip(start_arr_half, end_arr_half[::-1]):
        result_sum += start_num * end_num
        
    return result_sum
