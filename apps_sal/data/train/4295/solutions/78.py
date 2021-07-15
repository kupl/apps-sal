def balanced_num(number):
    middle = len(str(number)) // 2 - 1 if len(str(number))%2 == 0 else len(str(number)) // 2
    first_half = [int(i) for i in str(number)][:middle]
    second_half = [int(i) for i in str(number)][::-1][:middle]
    return 'Balanced' if sum(first_half) == sum(second_half) or number < 100 else 'Not Balanced'
