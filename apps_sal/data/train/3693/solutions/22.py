def make_negative(number):
    if str(number).startswith("-"):
        return number
    elif str(number).startswith("0"):
        return number
    else:
        return int("-" + str(number))
