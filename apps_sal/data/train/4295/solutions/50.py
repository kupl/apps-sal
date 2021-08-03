def balanced_num(number):
    array = [int(x) for x in str(number)]
    if len(array) % 2 == 0:
        print(len(array) // 2)
        print(sum(array[0: len(array) // 2 - 1]))
        if sum(array[0: (len(array) // 2 - 1)]) == sum(array[(len(array) // 2 + 1)::]):
            return 'Balanced'
        return 'Not Balanced'
    if sum(array[0: (len(array) // 2)]) == sum(array[(len(array) // 2) + 1::]):
        return 'Balanced'
    return 'Not Balanced'
