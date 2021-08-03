def strong_num(number):
    total = 0
    for n in str(number):
        total += factorial(n)
    return "STRONG!!!!" if total == number else "Not Strong !!"


def factorial(number):
    number = int(number)
    if number < 2:
        return 1
    else:
        return number * factorial(number - 1)
