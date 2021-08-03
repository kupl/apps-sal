import math


def loose_change(cents):
    if cents < 0:
        cents = 0
    cents = int(cents)

    change = {}

    change['Quarters'] = cents // 25
    cents = cents % 25

    change['Dimes'] = cents // 10
    cents = cents % 10

    change['Nickels'] = cents // 5
    cents = cents % 5

    change['Pennies'] = cents

    return change
