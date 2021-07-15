def odd_ones_out(numbers):
    temp = []
    count = 0
    for i in range(len(numbers)):
        count = numbers.count(numbers[i])
        if count % 2 == 0:
            temp.append(numbers[i])
    return temp
