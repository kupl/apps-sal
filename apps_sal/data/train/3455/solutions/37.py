def disarium_number(number):
    res = []
    for index, value in enumerate(str(number)):
        res.append(int(value) ** (index+1))
    return "Disarium !!" if sum(res) == number else "Not !!"
