def how_many_measurements(n):
    if n == 1:
        return 0
    elif n <= 3:
        return 1
    n_coins_in_sub_group = n / 3
    return how_many_measurements(n_coins_in_sub_group) + 1
