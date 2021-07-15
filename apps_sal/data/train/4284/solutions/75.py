def array_leaders(numbers):
    rightsum = 0
    i = len(numbers) - 1
    leaders = []
    while i > -1:
        if numbers[i] > rightsum:
            leaders.append(numbers[i])
        rightsum += numbers[i]
        i -= 1
    leaders.reverse()
    return leaders
