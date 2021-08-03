def divisible_by_three(st):
    num_str = str(st)
    sum = 0
    # iterate and add the numbers up
    for i in range(0, len(num_str)):
        sum += int(num_str[i])
    # check if numbers are divisible by 3
    if sum % 3 == 0:
        return True
    else:
        return False
    pass
