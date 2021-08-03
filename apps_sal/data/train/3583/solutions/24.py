def binary_array_to_number(arr):
    total = 0

    for n in range(len(arr)):
        if arr[n] == 1:
            total += pow(2, len(arr) - 1 - n)
    return total
