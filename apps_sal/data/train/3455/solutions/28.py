def disarium_number(number):
    list_number = list(str(number))
    result = 0
    for i, num in enumerate(list_number):
        result += int(num) ** (i + 1)
    return "Disarium !!" if result == number else "Not !!"
        

