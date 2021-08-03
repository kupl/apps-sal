def divisible_by(numbers, divisor):
    l = []
    l = numbers
    c = []
    for i in l:
        if(i % divisor == 0):
            c.append(i)
    return c
