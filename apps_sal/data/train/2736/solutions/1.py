def largest_arrangement(numbers):
    numbers = list(map(str, numbers))
    for x in range(len(numbers)):
        for j in range(len(numbers)):
            ab = numbers[x] + numbers[j]
            ba = numbers[j] + numbers[x]
            if int(ab) > int(ba):
                numbers[x], numbers[j] = numbers[j], numbers[x]
    return int(''.join(numbers))
