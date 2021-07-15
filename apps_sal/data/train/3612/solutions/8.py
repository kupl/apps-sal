def loose_change(coins_list, amount_of_change):
    changes = [1 if n+1 in coins_list else amount_of_change*2 for n in range(amount_of_change)]
    for i in range(amount_of_change):
        for c in coins_list:
            if i+c<amount_of_change: changes[i+c] = min(changes[i+c],changes[i]+1)
    return changes[amount_of_change-1]
