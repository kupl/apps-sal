def validate(n):
    list = []
    for (index, number) in enumerate(reversed(str(n))):
        list.append(int(number) * 2 if index % 2 != 0 else int(number))
    return sum([digit - 9 if digit > 9 else digit for digit in list]) % 10 == 0
