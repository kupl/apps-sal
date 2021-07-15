def disarium_number(number):
    power = 0
    res = 0
    numbers = [int(i) for i in str(number)]
    for i, v in enumerate(numbers):
        power = v**(i+1)
        res += power
    return "Disarium !!" if res == number else "Not !!"
