def make_negative(number):
    # Check for negative:
    if number < 0:
        return number
    # Check for positivce
    elif number > 0:
        return number * -1
    # Check for 0
    else:
        return 0
