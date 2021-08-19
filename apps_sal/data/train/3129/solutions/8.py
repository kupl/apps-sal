def divisible_by_three(string):
    return not sum((int(n) for n in string)) % 3
