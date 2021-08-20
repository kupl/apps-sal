def loose_change(cents):
    total_cents = 0
    denomination_list = [['Quarters', 25], ['Dimes', 10], ['Nickels', 5], ['Pennies', 1]]
    change_dict = {}
    for denomination in denomination_list:
        coin_count = 0
        while total_cents + denomination[1] <= cents:
            total_cents += denomination[1]
            coin_count += 1
        change_dict[denomination[0]] = coin_count
    return change_dict
