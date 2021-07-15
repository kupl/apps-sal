def loose_change(coins_list, amount_of_change):   
    n, i, t = 0, 0, amount_of_change
    coins_list.sort(reverse = True)
    while amount_of_change >= 0 and i < len(coins_list): 
        if amount_of_change - coins_list[i] >= 0: 
            n += 1
            amount_of_change -= coins_list[i]
        else: i += 1
    return min([int(t/i) for i in coins_list if t % i == 0] + [n])
    
'''
second version
def loose_change(coins_list, amount_of_change):   
    coins, i, t = 0, 0, amount_of_change
    coins_list.sort(reverse = True)
    while amount_of_change > 0:
        tem = divmod(amount_of_change, coins_list[i])
        coins += tem[0]
        amount_of_change -= tem[0]*coins_list[i]
        i += 1
    aa = [int(t/i) for i in coins_list if t % i == 0] + [coins]
    return min(aa)
'''
