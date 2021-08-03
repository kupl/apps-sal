def balanced_num(number):
    mid = len(str(number))
    if mid % 2 == 0:
        if sum(int(i) for i in str(number)[:(mid // 2) - 1]) == sum(int(i) for i in str(number)[(mid // 2 + 1):]):
            return 'Balanced'
        else:
            return 'Not Balanced'
    else:
        if sum(int(i) for i in str(number)[:(mid // 2)]) == sum(int(i) for i in str(number)[(mid // 2) + 1:]):
            return 'Balanced'
        else:
            return 'Not Balanced'
