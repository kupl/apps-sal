def am_I_afraid(day, num):
    if day == "Monday" and num == 12:
        return True
    if day == "Tuesday" and num > 95:
        return True
    if day == "Wednesday" and num == 34:
        return True
    if day == "Thursday" and num == 0:
        return True
    if day == "Friday" and num % 2 == 0:
        return True
    if day == "Saturday" and num == 56:
        return True
    if day == "Sunday" and abs(num) == 666:
        return True
    return False
