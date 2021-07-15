def array_leaders(numbers):
    sum = 0
    lst = list()
    numbers = numbers[::-1]
    for i in numbers:
        if i > sum:
            lst.append(i)
        sum += i
    return lst[::-1]
