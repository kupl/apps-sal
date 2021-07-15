def array_leaders(numbers):
    num = []
    for i in range(len(numbers)):
        if numbers[i] > sum(numbers[i+1:]):
            num.append(numbers[i])
    return num
