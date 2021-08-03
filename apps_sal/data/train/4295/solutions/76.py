def balanced_num(number):
    CountNombers = len(str(number)) // 2 - 1 if len(str(number)) % 2 == 0 else len(str(number)) // 2
    LeftPart = [int(k) for k in str(number)[:CountNombers]]
    RightPart = [int(k) for k in str(number)[:CountNombers: -1]]
    return 'Balanced' if sum(LeftPart) == sum(RightPart) and len(LeftPart) == len(RightPart) or \
        sum(LeftPart) == sum(RightPart[:-1]) and len(LeftPart) == len(RightPart) - 1 else 'Not Balanced'
