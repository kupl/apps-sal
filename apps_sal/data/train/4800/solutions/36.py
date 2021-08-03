def hotpo(n):
    algorithm_move_counter = 0
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        elif n % 2 > 0:
            n = (n * 3) + 1
        algorithm_move_counter += 1
    return algorithm_move_counter
