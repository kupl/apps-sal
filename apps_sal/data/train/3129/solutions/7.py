def divisible_by_three(st):
    sum = 0
    while int(st) > 0:
        digit = int(st) % 10
        sum = sum + digit
        st = int(st) // 10
    if sum % 3 == 0:
        return True
    else:
        return False
