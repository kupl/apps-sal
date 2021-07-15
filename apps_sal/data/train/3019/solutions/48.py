def str_count(string, letter):
    amount = 0
    for l in string:
        if l == letter:
            amount += 1
    return amount

