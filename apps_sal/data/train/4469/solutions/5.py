def is_narcissistic(i):
    numbers = list(str(i))
    power = len(str(i))
    sum = 0

    for number in numbers:
        sum += (int(number) ** power)

    return sum == i
    
    


