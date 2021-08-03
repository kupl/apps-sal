def odd_ones_out(numbers):
    temp = []
    for num in numbers:
        if (numbers.count(num) % 2 == 0):
            temp.append(num)
    return temp
