def disarium_number(number):
    total = 0
    res = list(str(number))
    count = 0
    for item in res:
        total += int(item) ** (count + 1)
        count += 1
    if total == number:
        return 'Disarium !!'
    else:
        return 'Not !!'
