def disarium_number(number):
    str_number = str(number)
    result = 0
    for i, num in enumerate(str_number):
        result += int(num) ** (i + 1)
    return "Disarium !!" if result == number else "Not !!"
