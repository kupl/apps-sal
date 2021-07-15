def even_or_odd(number):
    if int(number/2) == float(number/2):
        return "Even"
    else:
        return "Odd"

num = 10024001232
print(even_or_odd(num))
