def disarium_number(number):
    sum = 0
    for k,v in enumerate(str(number)):
        sum += int(v) ** (k+1)
    return "Disarium !!" if sum == number else "Not !!"
