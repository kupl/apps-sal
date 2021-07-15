def sum_mix(arr):
    i = 0
    array_numbers = []
    for i in range(len(arr)):
        array_numbers.append(int(arr[i]))
        i = i + 1
    return sum(array_numbers)
