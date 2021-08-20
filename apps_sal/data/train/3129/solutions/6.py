def divisible_by_three(st):
    num_str = str(st)
    sum = 0
    for i in range(0, len(num_str)):
        sum += int(num_str[i])
    if sum % 3 == 0:
        return True
    else:
        return False
    pass
