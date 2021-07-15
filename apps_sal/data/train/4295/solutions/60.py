def balanced_num(number):
    num = str(number)
    if len(num) < 3:
        return 'Balanced'
    size = len(num) // 2 - (not len(num) % 2)
    lsum = sum(map(int, num[:size]))
    rsum = sum(map(int, num[-size:]))
    return 'Balanced' if lsum == rsum else 'Not Balanced'
