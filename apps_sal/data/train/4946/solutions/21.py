def house_numbers_sum(arr):
    sum = 0
    for i in range(len(arr)):
        if(arr[i] == 0):
            break
        else:
            sum += arr[i]
    return sum
