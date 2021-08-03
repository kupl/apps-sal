def thirt(n):
    sequence = [1, 10, 9, 12, 3, 4]
    numbers = str(n)[::-1]
    sum = 0
    for i in range(len(numbers)):
        sum += int(sequence[i % 6]) * int(numbers[i])
    if sum == n:
        return sum
    else:
        return thirt(sum)
