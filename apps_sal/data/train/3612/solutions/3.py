def loose_change(coins_list, amount_of_change):
    if len(coins_list) == 1: return amount_of_change
    return min(
        loose_change(coins_list[:-1], amount_of_change),
        amount_of_change // coins_list[-1] + loose_change(coins_list[:-1], amount_of_change % coins_list[-1])
    )
