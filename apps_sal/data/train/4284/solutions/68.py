def array_leaders(numbers):
    leaders = []
    while numbers:
        if numbers[0] > sum(numbers) - numbers[0]:
            leaders.append(numbers[0])
        numbers.remove(numbers[0])
    return leaders
