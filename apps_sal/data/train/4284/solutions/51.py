def array_leaders(numbers):
    leaders = []
    for i in range(len(numbers) - 1):
        if numbers[i] > sum(numbers[i + 1:-1]) + numbers[-1]:
            leaders.append(numbers[i])
        else:
            continue
    if numbers[-1] > 0:
        leaders.append(numbers[-1])
    return leaders
