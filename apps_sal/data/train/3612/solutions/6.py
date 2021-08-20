def loose_change(coins_list, amount_of_change):
    coins_amount = [0] + [float('inf')] * amount_of_change
    for i in range(1, amount_of_change + 1):
        coins_amount[i] = min((coins_amount[i - c] for c in coins_list if c <= i)) + 1
    return coins_amount[-1]
