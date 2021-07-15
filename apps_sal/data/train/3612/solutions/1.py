def loose_change(coins_list, amount):
    solution = [0] + [amount + 1] * amount
    for atmc in range(1, amount + 1):
        for coin in coins_list:
            if coin <= atmc:
                solution[atmc] = min(solution[atmc], solution[atmc - coin] + 1)
    return -1 if solution[amount] > amount else solution[amount]
