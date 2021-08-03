def balanced_num(number):
    number = str(number)
    if len(number) == 1:
        return 'Balanced'
    if len(number) % 2 == 1:
        return 'Balanced' if sum(int(i) for i in number[:len(number) // 2]) == sum(int(i) for i in number[len(number) // 2 + 1:]) else 'Not Balanced'
    else:
        return 'Balanced' if sum(int(i) for i in number[:len(number) // 2 - 1]) == sum(int(i) for i in number[len(number) // 2 + 1:]) else 'Not Balanced'
