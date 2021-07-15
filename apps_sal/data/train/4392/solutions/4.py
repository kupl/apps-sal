def find_lowest_int(number):
    multiplier = 1
    while sorted(str(number * multiplier)) != sorted(str((number + 1) * multiplier)):
        multiplier += 1
    return multiplier
