def disarium_number(number):
    tmp = number
    arr = []
    while tmp > 0:
        arr.append(tmp % 10)
        tmp //= 10
    total = 0
    l = len(arr)
    for i in range(l):
        total += arr[i] ** (l - i)
    if total == number:
        return 'Disarium !!'
    return 'Not !!'
