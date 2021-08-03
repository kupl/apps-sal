from itertools import combinations_with_replacement as combos


def loose_change(coins_list, amount_of_change):
    least_list = []
    for x in range(len(coins_list)):
        for combo in combos(coins_list, x + 1):
            if sum(combo) == amount_of_change:
                least_list.append(len(combo))
    return min(least_list)
