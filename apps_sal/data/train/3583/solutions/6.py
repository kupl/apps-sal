def binary_array_to_number(arr):
    no_of_elements = len(arr)
    k = no_of_elements
    sum = 0
    while k != 0:
        sum = sum + arr[no_of_elements - k] * 2 ** (k - 1)
        k = k - 1
    return sum
