from numpy import diff


def jumping_number(number):
    return "Jumping!!" if all([abs(x) == 1 for x in diff([int(x) for x in str(number)])]) else "Not!!"
