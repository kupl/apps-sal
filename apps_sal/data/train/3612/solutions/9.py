def loose_change(coins_list, amount_of_change):
    if amount_of_change == 0:
        return 0
    elif amount_of_change < 0 or len(coins_list) == 0:
        return float('inf')
    else:
        with_first_coin = loose_change(coins_list, amount_of_change - coins_list[-1])
        without_first_coin = loose_change(coins_list[:-1], amount_of_change)
        return min(with_first_coin + 1, without_first_coin)
