def min_value(digits):
    digits_arr = []
    minimum = ''

    for i in range(len(digits)):
        digits_arr.append(int(digits[i]))
    
    sorted_arr = sorted(set(digits_arr))
    
    for j in range(len(sorted_arr)):
        minimum += str(sorted_arr[j])
    
    return int(minimum)
