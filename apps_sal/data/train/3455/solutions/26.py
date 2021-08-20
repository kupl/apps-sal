def disarium_number(number):
    numArr = str(number)
    mySum = 0
    i = 1
    for num in numArr:
        mySum += int(num) ** i
        i = i + 1
    if mySum == number:
        return 'Disarium !!'
    else:
        return 'Not !!'
