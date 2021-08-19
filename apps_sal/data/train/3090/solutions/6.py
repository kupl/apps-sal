def find_2nd_largest(arr):
    SECOND_lARGEST = -2
    arr_set = set(arr)
    numbers = sorted((number for number in arr_set if type(number) == int))
    return numbers[SECOND_lARGEST] if len(numbers) > 1 else None
