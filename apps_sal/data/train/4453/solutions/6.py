def shortest_steps_to_num(n):
    step = 0
    while n > 1:
        n, step = n // 2, step + 1 + n % 2
    return step
