def happy_numbers(n):
    HappyNumbers = []
    for i in range(n + 1):
        AlreadyGoneThrough = []
        a = i
        while a != 1 and a not in AlreadyGoneThrough:
            b = 0
            AlreadyGoneThrough.append(a)
            for digit in str(a):
                b = b + int(digit) ** 2
            a = b
        if a in AlreadyGoneThrough:
            pass
        elif a == 1:
            HappyNumbers.append(i)
    return HappyNumbers
