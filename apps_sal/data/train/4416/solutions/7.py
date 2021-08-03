from math import floor


def loose_change(cents):
    change_dict = {}
    cents = 0 if cents < 0 else floor(cents)
    change_dict["Quarters"] = cents // 25
    cents %= 25
    change_dict["Dimes"] = cents // 10
    cents %= 10
    change_dict["Nickels"] = cents // 5
    cents %= 5
    change_dict["Pennies"] = cents
    return change_dict
