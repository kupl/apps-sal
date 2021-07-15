def array_plus_array(arr1,arr2):
    counter_one = 0
    counter_two = 0
    for integers in arr1:
        counter_one = counter_one + integers
    for integers in arr2:
        counter_two = counter_two + integers
    output = counter_one + counter_two
    return output
