def square_sum(numbers):
    sums = 0
    for num in range(len(numbers)):
        sums += pow(numbers[num], 2)
    return sums
