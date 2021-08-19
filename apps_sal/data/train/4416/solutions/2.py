def loose_change(cents):
    coins = {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    if cents <= 0:
        return coins
    coins['Quarters'] = cents // 25
    coins['Dimes'] = cents % 25 // 10
    coins['Nickels'] = cents % 25 % 10 // 5
    coins['Pennies'] = cents % 25 % 10 % 5 // 1
    return coins
