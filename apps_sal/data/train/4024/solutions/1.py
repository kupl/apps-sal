SPECIAL = set('012345')


def special_number(number):
    return "Special!!" if set(str(number)) <= SPECIAL else "NOT!!"
