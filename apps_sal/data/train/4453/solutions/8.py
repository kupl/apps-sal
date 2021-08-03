def shortest_steps_to_num(num):
    steps = 0
    while num > 1:
        if num % 2 == 0:
            num = num // 2
        elif num == 3:
            num -= 1
        else:
            num -= 1
        steps += 1
    return steps
