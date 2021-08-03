def hotpo(n):
    count = 0
    number = n
    while number != 1:
        if number % 2 == 0:
            number = number / 2
        elif number % 2 != 0:
            number = 3 * number + 1
        count += 1
    return count
