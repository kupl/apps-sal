def balanced_num(number):
    if len(str(number)) % 2 == 1:
        mid = len(str(number)) // 2
        return 'Balanced' if sum([int(x) for x in str(number)[:mid]]) == sum([int(x) for x in str(number)[mid + 1:]]) else 'Not Balanced'
    else:
        mid = mid = len(str(number)) // 2
        return 'Balanced' if sum([int(x) for x in str(number)[:mid - 1]]) == sum([int(x) for x in str(number)[mid + 1:]]) else 'Not Balanced'
