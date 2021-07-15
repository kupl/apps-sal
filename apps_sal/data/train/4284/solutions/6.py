def array_leaders(numbers):
    a = []
    numbers.append(0)
    for i in range(len(numbers)):
        if numbers[i] > sum(numbers[i+1:]):
            a.append(numbers[i])
    return a

