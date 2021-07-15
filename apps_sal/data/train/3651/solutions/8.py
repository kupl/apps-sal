def square(number):
    a = []
    sum = 1
    while len(a) < number:
        a.append(sum)
        sum = sum + sum
    return a[-1]
