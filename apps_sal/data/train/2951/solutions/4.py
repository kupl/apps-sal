def how_many_measurements(n):
    # Split coins in three equal sized groups,
    # one measurement will tell which of the groups contains
    # the fake coin, when less than 3 coins is in a group, one
    # measurement is required to determine which coin is fake
    if n == 1:
        return 0
    elif n <= 3:
        return 1
    n_coins_in_sub_group = n / 3
    return how_many_measurements(n_coins_in_sub_group) + 1
