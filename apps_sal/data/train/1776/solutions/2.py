def roll_dice(rolls, sides, threshold):
    divisor = sides ** rolls
    stack = [1 for i in range(sides)]
    for i in range(1, rolls):
        nstack = [0 for j in range(len(stack) + sides - 1)]
        for j in range(len(nstack)):
            start = j - sides + 1
            if start < 0:
                start = 0
            end = j
            if end >= len(stack):
                end = len(stack) - 1
            nstack[j] = sum(stack[start:end + 1])
        stack = nstack
    divend = sum(stack[threshold - rolls:])
    return divend / divisor
