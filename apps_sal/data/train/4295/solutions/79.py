def balanced_num(number):
    list = [int(digits) for digits in str(number)]
    even_lower = len(list) // 2 - 1
    even_upper = len(list) // 2
    index_odd = (len(list) - 1) // 2
    for nums in list:
        if len(list) % 2 == 0:
            if sum(list[:even_lower]) == sum(list[even_upper + 1:]):
                return 'Balanced'
            else:
                return 'Not Balanced'
        if len(list) % 2 == 1:
            if sum(list[:index_odd]) == sum(list[index_odd + 1:]):
                return 'Balanced'
            else:
                return 'Not Balanced'
