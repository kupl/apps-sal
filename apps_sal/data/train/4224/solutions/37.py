def dont_give_me_five(start, end):
    array = list(range(start, end + 1))
    array_str = [str(num) for num in array]
    array_with_5 = [num for num in array_str if '5' in num]

    count_withno5 = len(array_str) - len(array_with_5)
    return count_withno5   # amount of numbers
