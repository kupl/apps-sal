def array_leaders(numbers):
    numbers.append(0)
    leaders = []
    for i in range(len(numbers) - 1):
        if numbers[i] > sum(numbers[i + 1: len(numbers)]):
            leaders.append(numbers[i])
    return leaders
