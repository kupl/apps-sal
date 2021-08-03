def shortest_steps_to_num(num):
    x = 0
    while num > 1:
        if num % 2:
            num -= 1
        else:
            num /= 2
        x += 1
    return x
