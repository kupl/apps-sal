def make_change(amount):
    result = {}
    if amount == 0:
        return result
    else:
        halves = amount // 50
        remainder = amount % 50
        quarters = remainder // 25
        remainder = remainder % 25
        dimes = remainder // 10
        remainder = remainder % 10
        nickels = remainder // 5
        pennies = remainder % 5
        if halves > 0:
            result['H'] = halves
        if quarters > 0:
            result['Q'] = quarters
        if dimes > 0:
            result['D'] = dimes
        if nickels > 0:
            result['N'] = nickels
        if pennies > 0:
            result['P'] = pennies
    return result
